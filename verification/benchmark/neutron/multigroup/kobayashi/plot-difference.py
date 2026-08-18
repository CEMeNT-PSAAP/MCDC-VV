import h5py
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import openmc
import os
import shutil

from matplotlib.colors import TwoSlopeNorm

# Get results
with h5py.File("mcdc/output_4.h5", "r") as f:
    fluxes_mcdc = f["tallies/tracklength_tally_0/flux/mean"][()]
    densities_mcdc = f["tallies/tracklength_tally_1/density/mean"][()]
    x = f["tallies/tracklength_tally_0/grid/x"][()]
    y = f["tallies/tracklength_tally_0/grid/y"][()]
    z = f["tallies/tracklength_tally_0/grid/z"][()]
    t = f["tallies/tracklength_tally_0/grid/time"][()]

# Get results
with openmc.StatePoint("openmc_/output_4.h5") as sp:
    tally = sp.get_tally(scores=["flux"])
    fluxes_openmc = tally.mean.reshape((100, 60, 100, 60))
    fluxes_openmc = np.swapaxes(fluxes_openmc, 1, 3)
    tally = sp.get_tally(scores=["inverse-velocity"])
    densities_openmc = tally.mean.reshape((100))

densities = abs(densities_mcdc - densities_openmc) / (
    0.5 * (densities_mcdc + densities_openmc)
)

# The grids
t_mid = 0.5 * (t[:-1] + t[1:])
XY_X, XY_Y = np.meshgrid(x, y, indexing="ij")
XZ_X, XZ_Z = np.meshgrid(x, z, indexing="ij")
YZ_Y, YZ_Z = np.meshgrid(y, z, indexing="ij")

# Create clean folder for output figures
# Check if the folder exists
if os.path.exists("differences"):
    shutil.rmtree("differences")  # Remove the existing folder
os.makedirs("differences")  # Create a new folder

# Iterate over time step and create figures
N = len(fluxes_mcdc)
for i in range(N):
    flux_mcdc = fluxes_mcdc[i]
    flux_openmc = fluxes_openmc[i]

    # The difference
    flux = np.zeros_like(flux_mcdc)

    num = flux_mcdc - flux_openmc
    denom = 0.5 * (flux_mcdc + flux_openmc)

    zero_mcdc = flux_mcdc == 0.0
    zero_openmc = flux_openmc == 0.0

    denom[zero_mcdc] = flux_openmc[zero_mcdc]
    denom[zero_openmc] = flux_mcdc[zero_openmc]

    idx = denom != 0.0

    flux[idx] = num[idx] / denom[idx]

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
    ax[0, 0].set_ylabel("Relative difference")
    ax[0, 0].set_xlabel("Time")
    ax[0, 0].set_title("Density")

    # Density point
    ax[0, 0].plot(t_mid[i], densities[i], "ro", fillstyle="none")

    # XY flux
    ax[0, 1].pcolormesh(XY_Y, XY_X, flux_z, cmap="RdBu_r", norm=TwoSlopeNorm(0))
    ax[0, 1].set_aspect("equal")
    ax[0, 1].set_xlabel(r"$y$")
    ax[0, 1].set_ylabel(r"$x$")
    ax[0, 1].invert_yaxis()
    ax[0, 1].set_title("Flux-XY (Top View)")

    # XZ flux
    ax[1, 0].pcolormesh(XZ_X, XZ_Z, flux_y, cmap="RdBu_r", norm=TwoSlopeNorm(0))
    ax[1, 0].set_aspect("equal")
    ax[1, 0].set_xlabel(r"$x$")
    ax[1, 0].set_ylabel(r"$z$")
    ax[1, 0].set_title("Flux-XZ (Front View)")

    # YZ flux
    ax[1, 1].pcolormesh(YZ_Y, YZ_Z, flux_x, cmap="RdBu_r", norm=TwoSlopeNorm(0))
    ax[1, 1].set_aspect("equal")
    ax[1, 1].set_xlabel(r"$y$")
    ax[1, 1].set_ylabel(r"$z$")
    ax[1, 1].set_title("Flux-YZ (Side View)")

    plt.suptitle("MC/DC and OpenMC relative difference")
    plt.savefig(
        f"differences/figure_{i:03}.png", dpi=300, bbox_inches="tight", pad_inches=0
    )
    plt.close()
