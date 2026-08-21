from pathlib import Path
import sys

import h5py
import matplotlib.pyplot as plt

from reference import reference

# Locate case data independently of the caller's working directory.
CASE_DIR = Path(__file__).resolve().parent
output = sys.argv[1]

# Analytical reference solution
z_ref, phi_ref = reference()

# Load results
with h5py.File(output, "r") as f:
    z = f["tallies/tracklength_tally_0/grid/z"][:]
    dz = z[1:] - z[:-1]
    z_mid = 0.5 * (z[:-1] + z[1:])
    phi = f["tallies/tracklength_tally_0/flux/mean"][:]
    phi_sd = f["tallies/tracklength_tally_0/flux/sdev"][:]

# Normalize
phi, phi_sd = phi / dz, phi_sd / dz

# Flux - spatial average
plt.plot(z_mid, phi, "-b", label="MC")
plt.fill_between(z_mid, phi - phi_sd, phi + phi_sd, alpha=0.2, color="b")
plt.plot(z_ref, phi_ref, "-r", label="Reference")
plt.xlabel(r"$z$, cm")
plt.ylabel("Flux")
plt.grid()
plt.legend()
plt.title(r"$\bar{\phi}_i$")
plt.savefig(CASE_DIR / "flux.png", dpi=200, bbox_inches="tight")
plt.close()
