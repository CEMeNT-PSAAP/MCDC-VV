"""Process one recorded VVP launch into an isolated results directory."""

import argparse
import datetime
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

REPO_DIR = Path(__file__).resolve().parent


# ======================================================================================
# Helper functions
# ======================================================================================


def get_launch_id(launch):
    """Return the stored launch ID or derive one for legacy metadata."""
    if "launch_id" in launch:
        return launch["launch_id"]

    launched_at = datetime.datetime.fromisoformat(launch["launched_at"])
    return launched_at.astimezone(datetime.UTC).strftime("%Y%m%dT%H%M%SZ")


def write_metadata(metadata_file, metadata):
    """Persist updated processing provenance."""
    with metadata_file.open("w") as f:
        yaml.dump(metadata, f, sort_keys=False)


# ======================================================================================
# Command-line arguments
# ======================================================================================

parser = argparse.ArgumentParser(description="Process a recorded MC/DC VVP launch.")
parser.add_argument(
    "launch_id",
    nargs="?",
    default=None,
    help="Metadata launch ID to process. Defaults to the latest launch.",
)
args = parser.parse_args()

# ======================================================================================
# Set up results
# ======================================================================================

results_dir = REPO_DIR / "results"
metadata_file = results_dir / "metadata.yaml"

if not metadata_file.is_file():
    raise FileNotFoundError(
        "Top-level launch metadata not found. Run launch.py before process.py."
    )

with metadata_file.open("r") as f:
    metadata = yaml.safe_load(f) or {}

launches = metadata.get("launches", [])
if not launches:
    raise ValueError(f"No launches are recorded in {metadata_file}")

if args.launch_id is None:
    launch = launches[-1]
else:
    matches = [item for item in launches if get_launch_id(item) == args.launch_id]
    if not matches:
        available = ", ".join(get_launch_id(item) for item in launches)
        raise ValueError(
            f"Launch ID '{args.launch_id}' was not found. Available launches: {available}"
        )
    launch = matches[-1]

launch_id = get_launch_id(launch)
launch_config = launch["launch_config"]
suite_runs = launch.get("suite_runs", {})
has_recorded_suite_runs = "suite_runs" in launch
launch_results = results_dir / launch_id
launch_results.mkdir(parents=True, exist_ok=True)

if not has_recorded_suite_runs:
    print(
        "Warning: this legacy launch does not record exact suite runs; "
        "each suite will process its latest Maestro run."
    )

print("=" * 80)
print(f"Processing launch : {launch_id}")
print(f"Launched at       : {launch['launched_at']}")
print(f"Results directory : {launch_results}")
print("=" * 80)


# ======================================================================================
# Process enabled suites
# ======================================================================================

for suite, options in launch_config.items():
    if not options.get("enabled", False):
        print(f"Skip disabled suite: {suite}")
        continue

    if options.get("platform") != launch.get("active_platform"):
        print(f"Skip suite not submitted by this launch: {suite}")
        continue

    if has_recorded_suite_runs and suite not in suite_runs:
        print(f"Skip suite without a recorded Maestro run: {suite}")
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

    suite_results = suite_dir / "results"

    # Prevent figures from a previous suite-processing run leaking into this launch.
    if suite_results.exists():
        shutil.rmtree(suite_results)

    command = [sys.executable, str(processor)]
    if suite in suite_runs:
        maestro_run = REPO_DIR / suite_runs[suite]
        if not maestro_run.is_dir():
            raise FileNotFoundError(f"Recorded Maestro run not found: {maestro_run}")
        command.append(str(maestro_run))

    subprocess.run(command, cwd=suite_dir, check=True)

    if not suite_results.is_dir():
        print(f"No suite results found: {suite_results}")
        continue

    destination = launch_results / suite
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        shutil.rmtree(destination)

    shutil.move(str(suite_results), str(destination))


# ======================================================================================
# Store processing metadata
# ======================================================================================

launch["launch_id"] = launch_id
launch["processed_at"] = datetime.datetime.now(datetime.UTC).isoformat()
launch["results_directory"] = str(launch_results.relative_to(REPO_DIR))
write_metadata(metadata_file, metadata)

with (launch_results / "metadata.yaml").open("w") as f:
    yaml.dump(launch, f, sort_keys=False)


# ======================================================================================
# Summary
# ======================================================================================

print()
print(f"Launch  : {launch_id}")
print(f"Results : {launch_results}")
print("Processing complete.")
