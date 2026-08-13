from pathlib import Path

import numpy as np

SHEM361_DATA = Path(__file__).resolve().parents[2] / "data" / "SHEM-361.npz"


def reference():
    # Load material data
    with np.load(SHEM361_DATA) as data:
        SigmaT = data["SigmaT"]
        SigmaC = data["SigmaC"]
        SigmaS = data["SigmaS"]
        nuSigmaF = data["nuSigmaF"]
        G = data["G"]
    SigmaT += SigmaC * 0.5

    A = np.diag(SigmaT) - SigmaS - nuSigmaF
    Q = np.zeros(G)
    Q[-1] = 1.0

    phi = np.linalg.solve(A, Q)
    return phi
