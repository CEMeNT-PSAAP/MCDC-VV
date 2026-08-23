"""Remove generated case outputs and processed figures from this suite."""

import shutil
from pathlib import Path

suite_dir = Path(__file__).resolve().parent

cases_dir = suite_dir / "cases"

# Remove simulation outputs and any figures left by interrupted processing.
for pattern in ("*/output*.h5", "*/*.png", "*/*.gif"):
    for generated_file in cases_dir.glob(pattern):
        generated_file.unlink()

# Remove the complete processed-results hierarchy.
results_dir = suite_dir / "results"
if results_dir.is_dir():
    shutil.rmtree(results_dir)

# Remove generated Maestro workflow directories.
for maestro_run in suite_dir.glob("maestro_run_*"):
    if maestro_run.is_dir():
        shutil.rmtree(maestro_run)
