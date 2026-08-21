import sys
from pathlib import Path

import h5py
import matplotlib.pyplot as plt
import numpy as np

from reference import reference

SHEM361_DATA = (
    Path(__file__).resolve().parents[3] / "fixed_source" / "data" / "SHEM-361.npz"
)

# Load the energy grid and one MC/DC result.
output_file = sys.argv[1]
with np.load(SHEM361_DATA) as data:
    energy = data["E"]
    energy_midpoint = 0.5 * (energy[1:] + energy[:-1])
    energy_width = np.diff(energy)

with h5py.File(output_file, "r") as output:
    flux = output["tallies/tracklength_tally_0/flux/mean"][:]
    flux_sdev = output["tallies/tracklength_tally_0/flux/sdev"][:]
    k_cycle = output["k_cycle"][:]
    k_mean = output["k_mean"][()]
    k_sdev = output["k_sdev"][()]
    N_inactive = int(output["settings/N_inactive"][()])

# Normalize the arbitrary eigenvector amplitude before comparing spectrum shapes.
k_reference, flux_reference = reference()
normalization = np.sum(flux)
flux /= normalization
flux_sdev /= normalization

flux = flux / energy_width * energy_midpoint
flux_sdev = flux_sdev / energy_width * energy_midpoint
flux_reference = flux_reference / energy_width * energy_midpoint

# Compare the MC/DC and analytical fundamental-mode energy spectra.
plt.plot(energy_midpoint, flux, "-b", label="MC/DC")
plt.fill_between(
    energy_midpoint,
    flux - flux_sdev,
    flux + flux_sdev,
    alpha=0.2,
    color="b",
)
plt.plot(energy_midpoint, flux_reference, "--r", label="analytical")
plt.xscale("log")
plt.xlabel(r"$E$, eV")
plt.ylabel(r"$E\phi(E)$")
plt.grid()
plt.legend()
plt.savefig("flux.png", dpi=200, bbox_inches="tight")
plt.close()

# Show convergence of the cycle estimates and distinguish active statistics.
cycles = np.arange(1, len(k_cycle) + 1)
active_cycles = cycles[N_inactive:]

plt.plot(cycles, k_cycle, "-b", label="MC/DC cycle")
plt.axhline(k_reference, color="k", linestyle="--", label="analytical")
plt.plot(
    active_cycles,
    np.full(active_cycles.size, k_mean),
    ":r",
    label="MC/DC active mean",
)
plt.fill_between(
    active_cycles,
    k_mean - k_sdev,
    k_mean + k_sdev,
    alpha=0.2,
    color="r",
)

if N_inactive > 0:
    plt.axvline(
        N_inactive + 0.5,
        color="0.5",
        linestyle=":",
        label="active cycles begin",
    )

plt.xlabel("Cycle")
plt.ylabel(r"$k$")
plt.grid()
plt.legend()
plt.savefig("k_history.png", dpi=200, bbox_inches="tight")
plt.close()
