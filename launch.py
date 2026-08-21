"""Launch configured VVP suites and record enough context to reproduce each run."""

import argparse
import datetime
import importlib.metadata
import subprocess
import sys
from pathlib import Path

import yaml

# ======================================================================================
# Bootstrap VVP imports
# ======================================================================================

REPO_DIR = Path(__file__).resolve().parent

# Support launching this script from any working directory without installing VVP.
if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))


# ======================================================================================
# Load launch configuration
# ======================================================================================

from configs.launch_config import LAUNCH_CONFIG

# ======================================================================================
# Helper functions
# ======================================================================================


def get_git_hash(repo_dir):
    """Return the commit that identifies the VVP source used for the launch."""
    return subprocess.check_output(
        ["git", "-C", str(repo_dir), "rev-parse", "HEAD"],
        stderr=subprocess.DEVNULL,
        text=True,
    ).strip()


def is_git_dirty(repo_dir):
    """Report whether the launch includes changes not captured by the commit hash."""
    result = subprocess.run(
        ["git", "-C", str(repo_dir), "status", "--porcelain"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        check=True,
    )
    return bool(result.stdout.strip())


def get_mcdc_version():
    """Return the installed MC/DC version when package metadata is available."""
    try:
        return importlib.metadata.version("mcdc")
    except importlib.metadata.PackageNotFoundError:
        return None


def write_metadata(metadata_file, metadata):
    """Persist launch metadata after each submission milestone."""
    with metadata_file.open("w") as f:
        yaml.dump(metadata, f, sort_keys=False)


# ======================================================================================
# Command-line arguments
# ======================================================================================

parser = argparse.ArgumentParser(description="Launch enabled MC/DC VVP suites.")
parser.add_argument(
    "--platform",
    default=None,
    help="Select suites configured for PLATFORM; omit for local run.",
)
args = parser.parse_args()

active_platform = args.platform


# ======================================================================================
# Set up results metadata
# ======================================================================================

results_dir = REPO_DIR / "results"
metadata_file = results_dir / "metadata.yaml"

results_dir.mkdir(parents=True, exist_ok=True)

# Preserve earlier launch records when adding the current campaign.
if metadata_file.is_file():
    with metadata_file.open("r") as f:
        metadata = yaml.safe_load(f) or {}
else:
    metadata = {}

metadata.setdefault("launches", [])

# Keep an append-only launch history so reruns do not erase provenance.
launch_time = datetime.datetime.now(datetime.UTC)
launch_record = {
    "launch_id": launch_time.strftime("%Y%m%dT%H%M%S%fZ"),
    "launched_at": launch_time.isoformat(),
    "active_platform": active_platform,
    "mcdc_version": get_mcdc_version(),
    "mcdc_vvp_hash": get_git_hash(REPO_DIR),
    "mcdc_vvp_dirty": is_git_dirty(REPO_DIR),
    "launch_config": LAUNCH_CONFIG,
    "suite_runs": {},
}
metadata["launches"].append(launch_record)

write_metadata(metadata_file, metadata)

print("=" * 80)
print("Prepared VVP results metadata")
print(f"Results directory : {results_dir}")
print(f"Metadata file     : {metadata_file}")
print(f"Launch ID         : {launch_record['launch_id']}")
print(f"Active platform   : {active_platform}")
print("=" * 80)


# ======================================================================================
# Launch enabled, compatible suites
# ======================================================================================

for suite, options in LAUNCH_CONFIG.items():
    if not options.get("enabled", False):
        print(f"Skip disabled suite: {suite}")
        continue

    suite_platform = options.get("platform")

    # Launch only suites explicitly assigned to this invocation's platform.
    if suite_platform != active_platform:
        print(
            f"Skip platform mismatch: {suite} "
            f"({suite_platform} != {active_platform})"
        )
        continue

    suite_dir = REPO_DIR / suite
    launcher = suite_dir / "launch.py"

    if not suite_dir.is_dir():
        raise FileNotFoundError(f"Suite directory not found: {suite_dir}")

    if not launcher.is_file():
        raise FileNotFoundError(f"Suite launcher not found: {launcher}")

    # Reuse the active interpreter so suite launchers inherit this environment.
    command = [
        sys.executable,
        str(launcher),
    ]

    # Forward only options that are meaningful for the configured suite.
    if suite_platform is not None:
        command.extend(["--platform", suite_platform])

    if options.get("N_node") is not None:
        command.extend(["--N_node", str(options["N_node"])])

    if options.get("walltime") is not None:
        command.extend(["--walltime", str(options["walltime"])])

    if options.get("rewrite", False):
        command.append("--rewrite")

    print("=" * 80)
    print(f"Launching suite: {suite}")
    print("Command:", " ".join(command))
    print("=" * 80)

    # Identify the Maestro directory created by this suite invocation.
    maestro_runs_before = set(suite_dir.glob("maestro_run_*"))
    subprocess.run(command, cwd=suite_dir, check=True)

    maestro_runs_after = set(suite_dir.glob("maestro_run_*"))
    new_maestro_runs = maestro_runs_after - maestro_runs_before

    if not new_maestro_runs:
        raise RuntimeError(f"Suite did not create a new Maestro run: {suite}")

    maestro_run = max(new_maestro_runs, key=lambda path: path.stat().st_mtime)
    launch_record["suite_runs"][suite] = str(maestro_run.relative_to(REPO_DIR))
    write_metadata(metadata_file, metadata)


# ======================================================================================
# Summary
# ======================================================================================

launch_record["submission_completed_at"] = datetime.datetime.now(
    datetime.UTC
).isoformat()
write_metadata(metadata_file, metadata)

print()
print(f"Launch ID: {launch_record['launch_id']}")
print("Launch complete.")
