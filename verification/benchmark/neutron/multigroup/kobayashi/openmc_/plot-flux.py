import h5py
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import openmc
import os
import shutil

# Get results
with openmc.StatePoint("output_4.h5") as sp:
    tally = sp.get_tally(scores=["flux"])
    fluxes = tally.mean.reshape((100, 60, 100, 60))
    fluxes = np.swapaxes(fluxes, 1, 3)
    tally = sp.get_tally(scores=["inverse-velocity"])
    densities = tally.mean.reshape((100))

# The grids
with h5py.File("../mcdc/output.h5", "r") as f:
    x = f["tallies/tracklength_tally_0/grid/x"][()]
    y = f["tallies/tracklength_tally_0/grid/y"][()]
    z = f["tallies/tracklength_tally_0/grid/z"][()]
    t = f["tallies/tracklength_tally_0/grid/time"][()]
t_mid = 0.5 * (t[:-1] + t[1:])
XY_X, XY_Y = np.meshgrid(x, y, indexing="ij")
XZ_X, XZ_Z = np.meshgrid(x, z, indexing="ij")
YZ_Y, YZ_Z = np.meshgrid(y, z, indexing="ij")

# Create clean folder for output figures
# Check if the folder exists
if os.path.exists("flux"):
    shutil.rmtree("flux")  # Remove the existing folder
os.makedirs("flux")  # Create a new folder

# Iterate over time step and create figures
N = len(fluxes)
for i in range(N):
    flux = fluxes[i]

    # Calculate flux averages
    flux_x = np.average(flux, axis=0)
    flux_y = np.average(flux, axis=1)
    flux_z = np.average(flux, axis=2)

    # Plot
    fig, ax = plt.subplots(
        2,
        2,
        figsize=(8, 6),
        gridspec_kw={"width_ratios": [1, 2], "height_ratios": [1, 1], "hspace": 0.5},
    )

    # Density curve
    ax[0, 0].plot(t_mid, densities, "b")
    ax[0, 0].set_yscale("log")
    ax[0, 0].set_ylabel("Density")
    ax[0, 0].set_xlabel("Time")
    ax[0, 0].set_title("Density")

    # Density point
    ax[0, 0].plot(t_mid[i], densities[i], "ro", fillstyle="none")

    # XY flux
    ax[0, 1].pcolormesh(XY_Y, XY_X, flux_z)
    ax[0, 1].set_aspect("equal")
    ax[0, 1].set_xlabel(r"$y$")
    ax[0, 1].set_ylabel(r"$x$")
    ax[0, 1].invert_yaxis()
    ax[0, 1].set_title("Flux-XY (Top View)")

    # XZ flux
    ax[1, 0].pcolormesh(XZ_X, XZ_Z, flux_y)
    ax[1, 0].set_aspect("equal")
    ax[1, 0].set_xlabel(r"$x$")
    ax[1, 0].set_ylabel(r"$z$")
    ax[1, 0].set_title("Flux-XZ (Front View)")

    # YZ flux
    ax[1, 1].pcolormesh(YZ_Y, YZ_Z, flux_x)
    ax[1, 1].set_aspect("equal")
    ax[1, 1].set_xlabel(r"$y$")
    ax[1, 1].set_ylabel(r"$z$")
    ax[1, 1].set_title("Flux-YZ (Side View)")

    plt.suptitle("OpenMC result")
    plt.savefig(f"flux/figure_{i:03}.png", dpi=300, bbox_inches="tight", pad_inches=0)
    plt.close()
