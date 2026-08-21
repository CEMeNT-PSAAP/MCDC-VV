"""Plot the spatial eigenfunction and cycle-by-cycle multiplication factor."""

import sys

import h5py
import matplotlib.pyplot as plt
import numpy as np

from reference import reference

output_file = sys.argv[1]

with h5py.File(output_file, "r") as output:
    z = output["tallies/tracklength_tally_0/grid/z"][:]
    flux = output["tallies/tracklength_tally_0/flux/mean"][:]
    flux_sdev = output["tallies/tracklength_tally_0/flux/sdev"][:]
    k_cycle = output["k_cycle"][:]
    k_mean = output["k_mean"][()]
    k_sdev = output["k_sdev"][()]
    N_inactive = int(output["settings/N_inactive"][()])

dz = np.diff(z)
z_midpoint = 0.5 * (z[:-1] + z[1:])
normalization = np.sum(flux)
flux = flux / dz / normalization
flux_sdev = flux_sdev / dz / normalization
k_reference, flux_reference = reference(z)

plt.plot(z_midpoint, flux, "-b", label="MC/DC")
plt.fill_between(
    z_midpoint,
    flux - flux_sdev,
    flux + flux_sdev,
    alpha=0.2,
    color="b",
)
plt.plot(z_midpoint, flux_reference, "--r", label="Reference")
plt.xlabel(r"$z$, cm")
plt.ylabel("Normalized scalar flux")
plt.grid()
plt.legend()
plt.savefig("flux.png", dpi=200, bbox_inches="tight")
plt.close()

cycles = np.arange(1, len(k_cycle) + 1)
active_cycles = cycles[N_inactive:]

plt.plot(cycles, k_cycle, "-b", label="MC/DC cycle")
plt.axhline(k_reference, color="k", linestyle="--", label="Reference")
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
