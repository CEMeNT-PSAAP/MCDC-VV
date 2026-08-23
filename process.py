"""Process registered VVP suites and collect their results."""

import shutil
import subprocess
import sys
from pathlib import Path

# ======================================================================================
# Bootstrap VVP imports
# ======================================================================================

REPO_DIR = Path(__file__).resolve().parent

# Support running this script from any working directory without installing VVP.
if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))


# ======================================================================================
# Load suite configuration
# ======================================================================================

from configs.launch_config import LAUNCH_CONFIG

# ======================================================================================
# Set up results
# ======================================================================================

results_dir = REPO_DIR / "results"
results_dir.mkdir(parents=True, exist_ok=True)


# ======================================================================================
# Process registered suites and collect their results
# ======================================================================================

for suite in LAUNCH_CONFIG:
    suite_dir = REPO_DIR / suite
    processor = suite_dir / "process.py"
    suite_results = suite_dir / "results"

    if not suite_dir.is_dir():
        raise FileNotFoundError(f"Suite directory not found: {suite_dir}")

    maestro_runs = list(suite_dir.glob("maestro_run_*"))

    # Generate suite results from the latest Maestro run when one is available.
    if processor.is_file() and maestro_runs:
        print("=" * 80)
        print(f"Processing suite: {suite}")
        print("=" * 80)
        subprocess.run(
            [sys.executable, str(processor)],
            cwd=suite_dir,
            check=True,
        )

    # Existing suite results remain collectable without a recorded Maestro run.
    if not suite_results.is_dir():
        print(f"Skip suite without processable results: {suite}")
        continue

    print("=" * 80)
    print(f"Collecting suite: {suite}")
    print("=" * 80)

    destination = results_dir / suite
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        shutil.rmtree(destination)

    shutil.move(str(suite_results), str(destination))


# ======================================================================================
# Summary
# ======================================================================================

print()
print(f"Results: {results_dir}")
print("Processing and collection complete.")
