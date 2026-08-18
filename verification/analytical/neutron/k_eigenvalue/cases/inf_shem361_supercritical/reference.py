from pathlib import Path

import numpy as np
from scipy.linalg import eig

SHEM361_DATA = (
    Path(__file__).resolve().parents[3] / "fixed_source" / "data" / "SHEM-361.npz"
)
CAPTURE_FACTOR = 1.0


def reference():
    """Return the dominant multiplication factor and normalized spectrum."""
    with np.load(SHEM361_DATA) as data:
        total = data["SigmaT"] + (CAPTURE_FACTOR - 1.0) * data["SigmaC"]
        loss = np.diag(total) - data["SigmaS"]
        production = data["nuSigmaF"]

    eigenvalues, eigenvectors = eig(production, loss)
    physical = np.isfinite(eigenvalues) & (np.abs(eigenvalues.imag) < 1.0e-10)
    indices = np.flatnonzero(physical)
    dominant = indices[np.argmax(eigenvalues[physical].real)]

    k_effective = float(eigenvalues[dominant].real)
    flux = eigenvectors[:, dominant].real
    if np.sum(flux) < 0.0:
        flux *= -1.0
    flux /= np.sum(flux)

    return k_effective, flux
