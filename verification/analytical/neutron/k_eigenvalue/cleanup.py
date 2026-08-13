"""Remove generated case outputs and processed figures from this suite."""

from pathlib import Path

suite_dir = Path(__file__).resolve().parent

for output in (suite_dir / "cases").glob("*/output*.h5"):
    output.unlink()

results_dir = suite_dir / "results"
if results_dir.is_dir():
    for figure in results_dir.glob("*.png"):
        figure.unlink()
