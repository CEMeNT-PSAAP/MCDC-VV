"""Collect available VVP suite results at the repository level."""

import shutil
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
# Collect available suite results
# ======================================================================================

for suite in LAUNCH_CONFIG:
    suite_dir = REPO_DIR / suite

    if not suite_dir.is_dir():
        raise FileNotFoundError(f"Suite directory not found: {suite_dir}")

    suite_results = suite_dir / "results"
    if not suite_results.is_dir():
        print(f"Skip suite without results: {suite}")
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
print("Collection complete.")
