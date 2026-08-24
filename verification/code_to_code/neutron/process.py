"""Process a completed neutron code-to-code Maestro study."""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

from util import particle_counts, require_reference_files

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
# Helper functions
# ======================================================================================


def clear_case_figures(case_dir):
    """Remove figures left by an earlier processing run."""
    for pattern in ("*.png", "*.gif"):
        for figure in case_dir.glob(pattern):
            figure.unlink()


def collect_case_figures(case_dir, destination, case_name, patterns):
    """Move generated case figures into a named suite results directory."""
    for pattern in patterns:
        for figure in case_dir.glob(pattern):
            figure.replace(destination / f"{case_name}_{figure.name}")


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

results_dir = suite_dir / "results"
convergence_dir = results_dir / "convergence"
comparison_dir = results_dir / "comparison"
reference_dir = results_dir / "reference"

# Start with an empty suite results hierarchy on every processing run.
if results_dir.is_dir():
    shutil.rmtree(results_dir)

convergence_dir.mkdir(parents=True, exist_ok=True)
comparison_dir.mkdir(parents=True, exist_ok=True)
reference_dir.mkdir(parents=True, exist_ok=True)

# Keep the effective launch and task definitions beside the processed figures.
shutil.copy2(launch_config_file, results_dir / "launch_config.yaml")
shutil.copy2(task_file, results_dir / "task.yaml")


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
    clear_case_figures(case_dir)

    # Generate and collect convergence figures over the particle-count study.
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
    collect_case_figures(
        case_dir,
        convergence_dir,
        case_name,
        ("convergence_*.png",),
    )
    collect_case_figures(
        case_dir,
        reference_dir,
        case_name,
        ("reference_*.png", "reference_*.gif"),
    )

    # Compare the participating codes at the largest shared sample size.
    counts = particle_counts(task["logN_min"], task["logN_max"], task["N_task"])
    mcdc_output = case_dir / f"output_{int(counts[-1])}.h5"
    reference_output = require_reference_files(case_dir, task["N_task"])[-1]
    plot_script = case_dir / "plot.py"
    subprocess.run(
        [
            sys.executable,
            str(plot_script),
            str(mcdc_output),
            str(reference_output),
            str(mcdc_output),
            str(reference_output),
        ],
        cwd=case_dir,
        check=True,
    )
    collect_case_figures(
        case_dir,
        comparison_dir,
        case_name,
        ("comparison.gif", "difference.gif"),
    )


# ======================================================================================
# Summary
# ======================================================================================

print()
print(f"Maestro run: {maestro_run}")
print(f"Platform   : {launch_config['platform']}")
print(f"Nodes      : {launch_config['N_node']}")
print(f"Processes  : {launch_config['N_process']}")
print(f"Cases      : {len(tasks)}")
print("Processing complete.")
