"""Download the canonical OpenMC reference outputs for the Kobayashi case."""

import hashlib
import urllib.request
from pathlib import Path

RECORD_ID = "15069882"
DOI = "10.5281/zenodo.15069882"
CHECKSUMS = {
    "output_0.h5": "09c9bb21ba70eaaca75d8e212ff09dca",
    "output_1.h5": "dedb2019a27fde10aa70af955720d227",
    "output_2.h5": "176ad33ba2dd3e8bbc48306a0c7cd173",
    "output_3.h5": "852e33bd30e7401b08d98ab0ca11965d",
    "output_4.h5": "936593f835c6127955723ff7a39d1352",
}


def checksum(path):
    """Return the MD5 checksum used by the Zenodo record."""
    digest = hashlib.md5()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def download_references():
    """Download and verify every OpenMC statepoint used by this case."""
    reference_dir = Path(__file__).resolve().parent / "reference"
    reference_dir.mkdir(exist_ok=True)

    for filename, expected_checksum in CHECKSUMS.items():
        destination = reference_dir / filename

        if destination.is_file() and checksum(destination) == expected_checksum:
            print(f"Reference is current: {destination}")
            continue

        temporary = reference_dir / f"{filename}.part"
        temporary.unlink(missing_ok=True)
        url = f"https://zenodo.org/records/{RECORD_ID}/files/{filename}?download=1"

        print(f"Downloading {url}")
        urllib.request.urlretrieve(url, temporary)

        actual_checksum = checksum(temporary)
        if actual_checksum != expected_checksum:
            temporary.unlink()
            raise ValueError(
                f"Checksum mismatch for {filename}: "
                f"expected {expected_checksum}, got {actual_checksum}"
            )

        temporary.replace(destination)
        print(f"Installed reference: {destination}")


if __name__ == "__main__":
    download_references()
