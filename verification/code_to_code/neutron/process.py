"""Process a completed neutron code-to-code Maestro study."""

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

# ======================================================================================
# Command-line arguments
# ======================================================================================

parser = argparse.ArgumentParser(
    description="Process the MC/DC VVP neutron code-to-code suite."
)
parser.add_argument(
    "maestro_run",
    nargs="?",
    default=None,
    help="Maestro run directory to process. Defaults to the latest maestro_run_*.",
)
args = parser.parse_args()


# ======================================================================================
# Paths
# ======================================================================================

suite_dir = Path(__file__).resolve().parent

if args.maestro_run is None:
    maestro_runs = sorted(
        suite_dir.glob("maestro_run_*"),
        key=lambda path: path.stat().st_mtime,
    )

    if not maestro_runs:
        raise FileNotFoundError("No maestro_run_* directory found.")

    maestro_run = maestro_runs[-1]
else:
    maestro_run = Path(args.maestro_run).expanduser()

    if not maestro_run.is_absolute():
        maestro_run = suite_dir / maestro_run

launch_config_file = maestro_run / "launch_config.yaml"
task_file = maestro_run / "task.yaml"

if not launch_config_file.is_file():
    raise FileNotFoundError(f"Launch config not found: {launch_config_file}")

if not task_file.is_file():
    raise FileNotFoundError(f"Task config not found: {task_file}")


# ======================================================================================
# Load configuration and tasks
# ======================================================================================

with launch_config_file.open("r") as f:
    launch_config = yaml.safe_load(f)

with task_file.open("r") as f:
    tasks = yaml.safe_load(f)


# ======================================================================================
# Process cases
# ======================================================================================

for case_name, task in tasks.items():
    case_dir = suite_dir / "cases" / case_name
    process_script = case_dir / "process.py"

    if not process_script.is_file():
        print(f"Skipping {case_name}: no process.py")
        continue

    print(f"Processing {case_name}")

    subprocess.run(
        [
            sys.executable,
            str(process_script),
            str(task["logN_min"]),
            str(task["logN_max"]),
            str(task["N_task"]),
        ],
        cwd=case_dir,
        check=True,
    )

    # Collect each case figure under a stable suite-level name.
    results_dir = suite_dir / "results"
    results_dir.mkdir(exist_ok=True)

    for figure in case_dir.glob("*.png"):
        destination = results_dir / f"{case_name}_{figure.name}"
        figure.replace(destination)


# ======================================================================================
# Summary
# ======================================================================================

print()
print(f"Maestro run: {maestro_run}")
print(f"Platform   : {launch_config['platform']}")
print(f"MPI        : {launch_config['mpi']}")
print(f"Rewrite    : {launch_config['rewrite']}")
print(f"Cases      : {len(tasks)}")
print("Processing complete.")
