import shutil
import subprocess
import sys
from pathlib import Path

# ======================================================================================
# Bootstrap VVP imports
# ======================================================================================

REPO_DIR = Path(__file__).resolve().parent

if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))


# ======================================================================================
# Load launch configuration
# ======================================================================================

from configs.launch_config import LAUNCH_CONFIG  # noqa: E402

# ======================================================================================
# Set up results
# ======================================================================================

results_dir = REPO_DIR / "results"

if not results_dir.is_dir():
    raise FileNotFoundError(
        "Top-level results directory not found. Run launch.py before process.py."
    )


# ======================================================================================
# Process enabled suites
# ======================================================================================

for suite, options in LAUNCH_CONFIG.items():
    if not options.get("enabled", False):
        print(f"Skip disabled suite: {suite}")
        continue

    suite_dir = REPO_DIR / suite
    processor = suite_dir / "process.py"

    if not suite_dir.is_dir():
        raise FileNotFoundError(f"Suite directory not found: {suite_dir}")

    if not processor.is_file():
        raise FileNotFoundError(f"Suite processor not found: {processor}")

    print("=" * 80)
    print(f"Processing suite: {suite}")
    print("=" * 80)

    subprocess.run(
        [sys.executable, str(processor)],
        cwd=suite_dir,
        check=True,
    )

    suite_results = suite_dir / "results"

    if not suite_results.is_dir():
        print(f"No suite results found: {suite_results}")
        continue

    destination = results_dir / suite
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        shutil.rmtree(destination)

    shutil.move(str(suite_results), str(destination))


# ======================================================================================
# Summary
# ======================================================================================

print()
print(f"Results : {results_dir}")
print("Processing complete.")
