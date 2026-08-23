"""Download the canonical OpenMC reference outputs for the C5G7 case."""

import hashlib
import urllib.request
from pathlib import Path

RECORD_ID = "15719118"
DOI = "10.5281/zenodo.15719118"
CHECKSUMS = {
    "output_0.h5": "d1c14f5174ab77b7a92d33cbf3378fba",
    "output_1.h5": "2c8adc956831a9d536e0455b7b2094af",
    "output_2.h5": "c40b4bbf34f92686594767e42e993b01",
    "output_3.h5": "d32b2e9fb039f2ac71b489d3d2b4cffc",
    "output_4.h5": "6cfbeedad4bae898b9b9678340312d44",
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
