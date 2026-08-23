"""Run one analytical k-eigenvalue case over its active-cycle study."""

import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np
import yaml

# ======================================================================================
# Command-line arguments
# ======================================================================================

parser = argparse.ArgumentParser(
    description="Run one MC/DC VVP analytical k-eigenvalue verification case."
)
parser.add_argument("--name", required=True, help="Verification case name.")
parser.add_argument("--task-file", default="task.yaml")
parser.add_argument(
    "--launcher",
    default="",
    help="Process launch command supplied by Maestro.",
)
args = parser.parse_args()


# ======================================================================================
# Paths and task definition
# ======================================================================================

suite_dir = Path(__file__).resolve().parent
case_dir = suite_dir / "cases" / args.name
task_file = suite_dir / args.task_file

if not case_dir.is_dir():
    raise FileNotFoundError(f"Case directory not found: {case_dir}")

with task_file.open("r") as f:
    tasks = yaml.safe_load(f)

if args.name not in tasks:
    raise ValueError(f"Case '{args.name}' is not listed in {task_file}")

task = tasks[args.name]


# ======================================================================================
# Run active-cycle tasks
# ======================================================================================

active_cycle_counts = np.rint(
    np.geomspace(
        task["N_active_min"],
        task["N_active_max"],
        task["N_task"],
    )
).astype(int)

for N_active in active_cycle_counts:
    N_active = int(N_active)

    output = f"output_{N_active}"
    output_file = case_dir / f"{output}.h5"

    if output_file.is_file():
        print(f"Skip existing output: {args.name}, N_active={N_active}")
        continue

    command = (
        f"{args.launcher} {sys.executable} input.py "
        "--mode=numba "
        f"--N_active={N_active} "
        f"--output={output} "
        "--no-progress_bar "
        "--caching"
    ).strip()

    print("=" * 80)
    print(f"Case    : {args.name}")
    print(f"N_active: {N_active}")
    print(f"Python  : {sys.executable}")
    print(f"Command : {command}")
    print("=" * 80)

    subprocess.run(command, shell=True, cwd=case_dir, check=True)
