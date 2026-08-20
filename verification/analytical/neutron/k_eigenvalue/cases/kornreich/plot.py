"""Plot the Kornreich eigenfunction and cycle-by-cycle multiplication factor."""

import sys

import h5py
import matplotlib.pyplot as plt
import numpy as np

from reference import REGION_EDGES, reference

output_file = sys.argv[1]

with h5py.File(output_file, "r") as output:
    x = output["tallies/tracklength_tally_0/grid/x"][:]
    flux = output["tallies/tracklength_tally_0/flux/mean"][:]
    flux_sdev = output["tallies/tracklength_tally_0/flux/sdev"][:]
    k_cycle = output["k_cycle"][:]
    k_mean = output["k_mean"][()]
    k_sdev = output["k_sdev"][()]
    N_inactive = int(output["settings/N_inactive"][()])

dx = np.diff(x)
x_midpoint = 0.5 * (x[:-1] + x[1:])
normalization = np.sum(flux)
flux = flux / dx / normalization
flux_sdev = flux_sdev / dx / normalization
k_reference, flux_reference = reference(x)

plt.plot(x_midpoint, flux, "-b", label="MC/DC")
plt.fill_between(
    x_midpoint,
    flux - flux_sdev,
    flux + flux_sdev,
    alpha=0.2,
    color="b",
)
plt.plot(x_midpoint, flux_reference, "--r", label="Reference")
for edge in REGION_EDGES[1:-1]:
    plt.axvline(edge, color="0.7", linewidth=0.8, linestyle=":")
plt.xlabel(r"$x$, cm")
plt.ylabel("Normalized scalar flux")
plt.grid()
plt.legend()
plt.show()

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
plt.show()
