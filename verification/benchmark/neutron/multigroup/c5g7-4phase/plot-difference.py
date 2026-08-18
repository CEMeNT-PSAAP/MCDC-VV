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
    fissions_mcdc = f["tallies/tracklength_tally_0/fission/mean"][()]
    x = f["tallies/tracklength_tally_0/grid/x"][()]
    y = f["tallies/tracklength_tally_0/grid/y"][()]
    z = f["tallies/tracklength_tally_0/grid/z"][()]
    t = f["tallies/tracklength_tally_0/grid/time"][()]

# Get results
Nt = 200
Nx = 17 * 2
Ny = 17 * 2
Nz = 17 * 6
with openmc.StatePoint("openmc_/output_4.h5") as sp:
    tally = sp.get_tally(name="pincell fission")
    fissions = tally.mean.reshape((Nt, Nz, Ny, Nx))
    fissions_openmc = np.swapaxes(fissions, 1, 3)

# Average of relative difference
diff = np.zeros_like(fissions_mcdc)
num = abs(fissions_mcdc - fissions_openmc)
denom = 0.5 * (fissions_mcdc + fissions_openmc)
#
zero_mcdc = fissions_mcdc == 0.0
zero_openmc = fissions_openmc == 0.0
#
denom[zero_mcdc] = fissions_openmc[zero_mcdc]
denom[zero_openmc] = fissions_mcdc[zero_openmc]
#
idx = denom != 0.0
diff[idx] = num[idx] / denom[idx]
diff_avg = np.average(diff, axis=(1, 2, 3)) * 100.0  # in %

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
N = len(fissions_mcdc)
for i in range(N):
    fission_mcdc = fissions_mcdc[i]
    fission_openmc = fissions_openmc[i]

    # The difference
    fission = np.zeros_like(fission_mcdc)

    num = fission_mcdc - fission_openmc
    denom = 0.5 * (fission_mcdc + fission_openmc)

    zero_mcdc = fission_mcdc == 0.0
    zero_openmc = fission_openmc == 0.0

    denom[zero_mcdc] = fission_openmc[zero_mcdc]
    denom[zero_openmc] = fission_mcdc[zero_openmc]

    idx = denom != 0.0

    fission[idx] = num[idx] / denom[idx]

    # Calculate fission averages
    fission_x = np.average(fission, axis=0)
    fission_y = np.average(fission, axis=1)
    fission_z = np.average(fission, axis=2)

    # Plot
    fig = plt.figure(figsize=(8, 5))
    gs = gridspec.GridSpec(
        2, 3, width_ratios=[0.7, 1, 1], height_ratios=[1, 1], hspace=0.5
    )

    ax1 = fig.add_subplot(gs[0, 0])  # Top-left
    ax2 = fig.add_subplot(gs[1, 0])  # Bottom-left
    ax3 = fig.add_subplot(gs[:, 1])  # Entire second column
    ax4 = fig.add_subplot(gs[:, 2])  # Entire third column

    # Total fission curve
    ax1.plot(t_mid, diff_avg, "b")
    ax1.set_yscale("log")
    ax1.set_ylabel("Avg. relative diff. (%)")
    ax1.set_xlabel("Time")
    ax1.set_title("Avg. relative diff.")
    # Total fission point
    ax1.plot(t_mid[i], diff_avg[i], "ro", fillstyle="none")

    # XY fission
    ax2.pcolormesh(XY_X, XY_Y, fission_z, cmap="RdBu_r", norm=TwoSlopeNorm(0))
    ax2.set_aspect("equal")
    ax2.set_xlabel(r"$x$")
    ax2.set_ylabel(r"$y$")
    ax2.set_title("Fission-XY")

    # XZ fission
    ax3.pcolormesh(XZ_X, XZ_Z, fission_y, cmap="RdBu_r", norm=TwoSlopeNorm(0))
    ax3.set_aspect("equal")
    ax3.set_xlabel(r"$x$")
    ax3.set_ylabel(r"$z$")
    ax3.set_title("Fission-XZ")
    pos = ax3.get_position()
    ax3.set_position(
        [pos.x0 + 0.02, pos.y0, pos.width, pos.height]
    )  # shift right by 0.02

    # YZ fission
    ax4.pcolormesh(YZ_Y, YZ_Z, fission_x, cmap="RdBu_r", norm=TwoSlopeNorm(0))
    ax4.set_aspect("equal")
    ax4.set_xlabel(r"$y$")
    ax4.set_ylabel(r"$z$")
    ax4.set_title("Fission-YZ")

    plt.suptitle("MC/DC and OpenMC relative difference")
    plt.savefig(
        f"differences/figure_{i:03}.png", dpi=300, bbox_inches="tight", pad_inches=0
    )
    plt.close()
