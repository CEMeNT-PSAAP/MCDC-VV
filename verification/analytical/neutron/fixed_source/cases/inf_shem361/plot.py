import numpy as np
import matplotlib.pyplot as plt
import h5py
import sys
from pathlib import Path

from reference import reference

SHEM361_DATA = Path(__file__).resolve().parents[2] / "data" / "SHEM-361.npz"

# Load results
output = sys.argv[1]
with np.load(SHEM361_DATA) as data:
    E = data["E"]
    G = data["G"]
    E_mid = 0.5 * (E[1:] + E[:-1])
    dE = E[1:] - E[:-1]
with h5py.File(output, "r") as f:
    phi = f["tallies/tracklength_tally_0/flux/mean"][:] / dE * E_mid
    phi_sd = f["tallies/tracklength_tally_0/flux/sdev"][:] / dE * E_mid

# Reference solution
phi_ref = reference() / dE * E_mid

# Flux
plt.plot(E_mid, phi, "-b", label="MC")
plt.fill_between(E_mid, phi - phi_sd, phi + phi_sd, alpha=0.2, color="b")
plt.plot(E_mid, phi_ref, "--r", label="analytical")
plt.xscale("log")
plt.xlabel(r"$E$, eV")
plt.ylabel(r"$E\phi(E)$")
plt.grid()
plt.legend()
plt.show()
