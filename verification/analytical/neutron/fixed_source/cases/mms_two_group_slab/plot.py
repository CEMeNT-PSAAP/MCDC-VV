"""Plot the fixed source and MC/DC-to-MMS solution comparison."""

import sys

import h5py
import matplotlib.pyplot as plt
import numpy as np

from reference import (
    LENGTH,
    TOTAL_SOURCE_STRENGTH,
    cell_average_scalar_flux,
    scalar_source,
)

output_file = sys.argv[1]

with h5py.File(output_file, "r") as output:
    x = output["tallies/tracklength_tally_0/grid/x"][:]
    flux = output["tallies/tracklength_tally_0/flux/mean"][:]
    flux_sdev = output["tallies/tracklength_tally_0/flux/sdev"][:]

dx = np.diff(x)
x_midpoint = 0.5 * (x[:-1] + x[1:])
flux = flux / dx
flux_sdev = flux_sdev / dx
reference = cell_average_scalar_flux(x)

for group in range(2):
    color = f"C{group}"
    plt.plot(x_midpoint, flux[group], color=color, label=f"MC/DC group {group + 1}")
    plt.fill_between(
        x_midpoint,
        flux[group] - flux_sdev[group],
        flux[group] + flux_sdev[group],
        color=color,
        alpha=0.2,
    )
    plt.plot(
        x_midpoint,
        reference[group],
        "--",
        color=color,
        label=f"MMS group {group + 1}",
    )

plt.xlabel(r"$x$, cm")
plt.ylabel("Scalar flux per source particle")
plt.grid()
plt.legend()
plt.savefig("flux.png", dpi=200, bbox_inches="tight")
plt.close()

x_plot = np.linspace(0.0, LENGTH, 201)
source = scalar_source(x_plot) / TOTAL_SOURCE_STRENGTH

for group in range(2):
    plt.plot(x_plot, source[group], label=f"Group {group + 1}")

plt.xlabel(r"$x$, cm")
plt.ylabel("Volume-source density per source particle")
plt.grid()
plt.legend()
plt.savefig("source.png", dpi=200, bbox_inches="tight")
plt.close()
