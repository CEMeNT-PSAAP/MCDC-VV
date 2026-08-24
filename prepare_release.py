"""Prepare flat GitHub release assets from collected VVP results."""

import shutil
from pathlib import Path

# ======================================================================================
# Paths
# ======================================================================================

REPO_DIR = Path(__file__).resolve().parent
RESULTS_DIR = REPO_DIR / "results"
RELEASE_DIR = REPO_DIR / "release"


# ======================================================================================
# Discover result figures
# ======================================================================================

if not RESULTS_DIR.is_dir():
    raise FileNotFoundError(f"Results directory not found: {RESULTS_DIR}")

figures = sorted(
    path
    for path in RESULTS_DIR.rglob("*")
    if path.is_file() and path.suffix.lower() in {".png", ".gif"}
)

if not figures:
    raise FileNotFoundError(f"No PNG or GIF results found in {RESULTS_DIR}")


# ======================================================================================
# Prepare flat release assets
# ======================================================================================

if RELEASE_DIR.is_dir():
    shutil.rmtree(RELEASE_DIR)
RELEASE_DIR.mkdir()

total_size = 0
for source in figures:
    relative_path = source.relative_to(RESULTS_DIR)
    asset_name = "--".join(relative_path.parts)
    destination = RELEASE_DIR / asset_name

    if destination.exists():
        raise FileExistsError(f"Flattened asset name is not unique: {destination.name}")

    shutil.copy2(source, destination)
    total_size += destination.stat().st_size
    print(f"{relative_path} -> {destination.name}")


# ======================================================================================
# Summary
# ======================================================================================

print()
print(f"Assets: {len(figures)}")
print(f"Size  : {total_size / 1024**2:.1f} MiB")
print(f"Release directory: {RELEASE_DIR}")
