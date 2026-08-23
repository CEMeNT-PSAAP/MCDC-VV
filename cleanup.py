"""Remove generated outputs and processed results from all registered VVP suites."""

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
# Clean registered suites
# ======================================================================================

for suite in LAUNCH_CONFIG:
    suite_dir = REPO_DIR / suite
    cleaner = suite_dir / "cleanup.py"

    if not suite_dir.is_dir():
        raise FileNotFoundError(f"Suite directory not found: {suite_dir}")

    if not cleaner.is_file():
        print(f"Skip suite without cleanup.py: {suite}")
        continue

    print("=" * 80)
    print(f"Cleaning suite: {suite}")
    print("=" * 80)

    subprocess.run(
        [sys.executable, str(cleaner)],
        cwd=suite_dir,
        check=True,
    )


# ======================================================================================
# Remove collected results
# ======================================================================================

results_dir = REPO_DIR / "results"
if results_dir.is_dir():
    shutil.rmtree(results_dir)


# ======================================================================================
# Summary
# ======================================================================================

print()
print("Cleanup complete.")
