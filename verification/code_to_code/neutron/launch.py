"""Build and launch the neutron code-to-code verification study with Maestro."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

import yaml

# ======================================================================================
# Bootstrap VVP imports
# ======================================================================================

REPO_DIR = Path(__file__).resolve().parents[3]

# Support launching this suite directly without installing MC/DC-VVP.
if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))


# ======================================================================================
# Load shared VVP configs
# ======================================================================================

from configs.platform_config import PLATFORMS
from configs.util import get_case_walltime

# User overrides are optional for local runs.
try:
    from configs.user_config import USER_CONFIG
except ImportError:
    USER_CONFIG = {}


# ======================================================================================
# Command-line arguments
# ======================================================================================

parser = argparse.ArgumentParser(
    description="Launch the MC/DC VVP neutron code-to-code suite."
)
parser.add_argument("--platform", default="local", choices=["local"] + list(PLATFORMS))
parser.add_argument(
    "--N_node",
    type=int,
    default=1,
    help="Set the number of compute nodes.",
)
parser.add_argument(
    "--walltime",
    type=float,
    default=None,
    help="Set the base walltime in hours; each case scales it by walltime_factor.",
)
parser.add_argument("--rewrite", action="store_true")
args = parser.parse_args()

if args.N_node < 1:
    parser.error("--N_node must be at least one.")

if args.platform == "local" and args.N_node != 1:
    parser.error("Local execution supports only --N_node 1.")


# ======================================================================================
# Paths
# ======================================================================================

suite_dir = Path(__file__).resolve().parent
task_file = suite_dir / "task.yaml"
run_case = suite_dir / "run_case.py"
study_file = suite_dir / "study.yaml"


# ======================================================================================
# Platform settings
# ======================================================================================

local = args.platform == "local"
user_platform_config = USER_CONFIG.get(args.platform, {})

mcdc_python = user_platform_config.get("mcdc_python")

# Use the active interpreter unless this platform specifies another MC/DC environment.
if mcdc_python is None:
    mcdc_python = sys.executable
else:
    mcdc_python = str(Path(mcdc_python).expanduser())

if not local:
    platform = PLATFORMS[args.platform]
    scheduler = platform["scheduler"]
    cpu_cores = platform["cpu_cores_per_node"]

    if args.N_node > platform["max_nodes"]:
        parser.error(
            f"--N_node exceeds the {platform['max_nodes']}-node limit for "
            f"{args.platform}."
        )

    account = user_platform_config.get("account")
    queue = user_platform_config.get("queue")
    reservation = user_platform_config.get("reservation")

    if account is None:
        raise ValueError(
            f"Platform '{args.platform}' requires an account. "
            "Create configs/user_config.py from configs/user_config.py.template."
        )


# ======================================================================================
# Load tasks
# ======================================================================================

with task_file.open("r") as f:
    tasks = yaml.safe_load(f)


# ======================================================================================
# Build Maestro study
# ======================================================================================

# Convert each configured case into one independent Maestro step.
steps = []
case_walltimes = {}

for case_name, task in tasks.items():
    # Normalize case names into stable Maestro step identifiers.
    safe_case_name = case_name.replace("-", "_")

    command = f"{mcdc_python} {run_case} --name {case_name}"

    # Maestro replaces LAUNCHER with the scheduler-specific process launcher.
    if not local:
        command += ' --launcher "$(LAUNCHER)"'

    if args.rewrite:
        command += " --rewrite"

    run = {"cmd": command}

    # Scheduled studies require explicit resources; local studies run directly.
    if not local:
        run["nodes"] = args.N_node
        walltime = get_case_walltime(task, platform, args.walltime)
        run["walltime"] = walltime
        case_walltimes[case_name] = walltime
        run["procs"] = args.N_node * cpu_cores
        run["exclusive"] = True

    steps.append(
        {
            "name": safe_case_name,
            "description": f"Run case: {case_name}",
            "run": run,
        }
    )

# Assemble the complete Maestro study from the generated case steps.
study = {
    "description": {
        "name": "maestro_run",
        "description": "MC/DC verification - neutron code-to-code suite",
    },
    "env": {
        "variables": {},
    },
    "study": steps,
}

if not local:
    # Attach batch settings only when Maestro submits to a scheduler.
    batch = {
        "type": scheduler,
        "host": platform["host"],
        "bank": account,
    }

    if queue is not None:
        batch["queue"] = queue

    if reservation is not None:
        batch["reservation"] = reservation

    study["batch"] = batch


# ======================================================================================
# Write Maestro study
# ======================================================================================

with study_file.open("w") as f:
    yaml.dump(study, f, sort_keys=False)


# ======================================================================================
# Launch Maestro
# ======================================================================================

maestro_python = None

if not local:
    maestro_python = user_platform_config.get("maestro_python")

env = os.environ.copy()

# Use the configured Maestro environment when it differs from the active one.
if maestro_python is None:
    maestro_command = ["maestro", "run", "study.yaml"]
else:
    maestro_python = Path(maestro_python).expanduser()
    maestro_bin = maestro_python.parent
    # Keep executables spawned by Maestro in the same configured environment.
    env["PATH"] = f"{maestro_bin}:{env['PATH']}"

    maestro_command = [
        str(maestro_python),
        "-m",
        "maestrowf.maestro",
        "run",
        "study.yaml",
    ]

subprocess.run(maestro_command, cwd=suite_dir, check=True, env=env)


# ======================================================================================
# Store launch metadata
# ======================================================================================

# Maestro creates timestamped run directories, so capture the newly generated launch.
maestro_runs = sorted(
    suite_dir.glob("maestro_run_*"),
    key=lambda path: path.stat().st_mtime,
)

if not maestro_runs:
    raise RuntimeError("Maestro did not create a maestro_run_* directory.")

latest_run = maestro_runs[-1]

launch_config = {
    "platform": args.platform,
    "scheduler": "local" if local else scheduler,
    "N_node": args.N_node,
    "N_process": 1 if local else args.N_node * cpu_cores,
    "walltime": args.walltime,
    "case_walltimes": case_walltimes,
    "rewrite": args.rewrite,
    "mcdc_python": mcdc_python,
}

# Snapshot the effective launch and task configuration with the generated run.
with (latest_run / "launch_config.yaml").open("w") as f:
    yaml.dump(launch_config, f, sort_keys=False)

with task_file.open("r") as f:
    task_config = yaml.safe_load(f)

with (latest_run / "task.yaml").open("w") as f:
    yaml.dump(task_config, f, sort_keys=False)


# ======================================================================================
# Summary
# ======================================================================================

print(f"Platform : {args.platform}")
print(f"Nodes    : {args.N_node}")
print(f"Rewrite  : {args.rewrite}")
print(f"Python   : {mcdc_python}")
print(f"Study    : {study_file}")

if not local:
    print(f"Scheduler: {scheduler}")
    print(f"Account  : {account}")
    print(f"Queue    : {queue}")
    print(f"Reserv.  : {reservation}")
    print("Walltimes:")
    for case_name, walltime in case_walltimes.items():
        print(f"  {case_name}: {walltime}")
    print(f"Procs    : {args.N_node * cpu_cores}")

print(f"Cases    : {len(steps)}")
