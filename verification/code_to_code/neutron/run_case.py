"""Run one neutron code-to-code case over its particle-count study."""

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

from util import particle_counts

# ======================================================================================
# Command-line arguments
# ======================================================================================

parser = argparse.ArgumentParser(
    description="Run one MC/DC VVP neutron code-to-code case."
)
parser.add_argument("--name", required=True, help="Verification case name.")
parser.add_argument("--task-file", default="task.yaml")
parser.add_argument(
    "--mpi",
    default="",
    help="MPI launch command supplied by Maestro, e.g. 'srun -n 112'.",
)
parser.add_argument(
    "--rewrite",
    action="store_true",
    help="Rewrite existing output files instead of skipping them.",
)
args = parser.parse_args()


# ======================================================================================
# Paths
# ======================================================================================

suite_dir = Path(__file__).resolve().parent
case_dir = suite_dir / "cases" / args.name
task_file = suite_dir / args.task_file

if not case_dir.is_dir():
    raise FileNotFoundError(f"Case directory not found: {case_dir}")


# ======================================================================================
# Load task definition
# ======================================================================================

with task_file.open("r") as f:
    tasks = yaml.safe_load(f)

if args.name not in tasks:
    raise ValueError(f"Case '{args.name}' is not listed in {task_file}")

task = tasks[args.name]


# ======================================================================================
# Run particle-count tasks
# ======================================================================================

for N_particle in particle_counts(
    task["logN_min"],
    task["logN_max"],
    task["N_task"],
):
    N_particle = int(N_particle)

    output = f"output_{N_particle}"
    output_file = case_dir / f"{output}.h5"

    if output_file.is_file():
        if args.rewrite:
            print(f"Rewrite (remove existing output): {args.name}, N={N_particle}")
            output_file.unlink()
        else:
            print(f"Skip (output exists): {args.name}, N={N_particle}")
            continue

    command = (
        f"{args.mpi} {sys.executable} input.py "
        f"--mode=numba "
        f"--N_particle={N_particle} "
        f"--output={output} "
        "--no-progress_bar "
        "--caching"
    ).strip()

    print("=" * 80)
    print(f"Case                : {args.name}")
    print(f"Particles per batch : {N_particle}")
    print(f"Python              : {sys.executable}")
    print(f"Command             : {command}")
    print("=" * 80)

    subprocess.run(
        command,
        shell=True,
        cwd=case_dir,
        check=True,
    )
