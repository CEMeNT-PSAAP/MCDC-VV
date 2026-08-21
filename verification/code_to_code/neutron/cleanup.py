"""Remove generated neutron code-to-code outputs and figures."""

from pathlib import Path

suite_dir = Path(__file__).resolve().parent

for output in suite_dir.glob("cases/*/output*.h5"):
    output.unlink()

for figure in suite_dir.glob("cases/*/*.png"):
    figure.unlink()

results_dir = suite_dir / "results"
if results_dir.is_dir():
    for figure in results_dir.glob("*.png"):
        figure.unlink()
