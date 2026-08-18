import h5py
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import openmc
import os
import shutil

# Get results
with openmc.StatePoint("openmc_/statepoint.30.h5") as sp:
    tally = sp.get_tally(scores=["flux"])
    flux_openmc = tally.mean.reshape((200, 500))
    sdev_openmc = tally.std_dev.reshape((200, 500))

with h5py.File("mcdc/output.h5", "r") as f:
    flux_mcdc = f["tallies/tracklength_tally_0/flux/mean"][()].transpose()
    sdev_mcdc = f["tallies/tracklength_tally_0/flux/sdev"][()].transpose()

    # Grids
    t = f["tallies/tracklength_tally_0/grid/time"][()]
    dt = t[1:] - t[:-1]
    t_mid = 0.5 * (t[1:] + t[:-1])

    E = f["tallies/tracklength_tally_0/grid/energy"][()]
    E_mid = 0.5 * (E[1:] + E[:-1])
    dE = E[1:] - E[:-1]

for i in range(200):
    y = E_mid * flux_openmc[i, :] / dE / dt[i]
    sd = E_mid * sdev_openmc[i, :] / dE / dt[i]
    plt.plot(E_mid, y, "r-", label="OpenMC")
    plt.fill_between(E_mid, y - sd, y + sd, alpha=0.2, color="r")

    y = E_mid * flux_mcdc[i, :] / dE / dt[i]
    sd = E_mid * sdev_mcdc[i, :] / dE / dt[i]
    plt.plot(E_mid, y, "b--", label="MC/DC")
    plt.fill_between(E_mid, y - sd, y + sd, alpha=0.2, color="b")

    plt.text(0.02, 0.9, f"$t$ $=$ {t_mid[i]:.3g} s", transform=plt.gca().transAxes)

    plt.xlabel("Energy [eV]")
    plt.ylabel(r"Spectrum, $E\phi(E, t)$")
    plt.xscale("log")
    plt.grid()
    plt.title("Pulsed Pincell: UO2 and Borated Water")

    plt.savefig(
        f"figures/figure_{i:03}.png", dpi=300, bbox_inches="tight", pad_inches=0
    )
    plt.close()
