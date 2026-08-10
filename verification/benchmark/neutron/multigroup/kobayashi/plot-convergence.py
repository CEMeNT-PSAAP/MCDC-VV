import h5py
import matplotlib.pyplot as plt
import numpy as np
import openmc
import os
import shutil

N_list = np.array([100000000, 316227766, 1000000000, 3162277660, 10000000000]) * 30

NN = len(N_list)

difference = np.zeros(NN)

# Getting the reference
with h5py.File("mcdc/output_4.h5", "r") as f:
    flux_mcdc = f["tallies/tracklength_tally_0/flux/mean"][()]
with openmc.StatePoint("openmc_/output_4.h5") as sp:
    tally = sp.get_tally(scores=["flux"])
    flux_openmc = tally.mean.reshape((100, 60, 100, 60))
    flux_openmc = np.swapaxes(flux_openmc, 1, 3)
zero_mcdc = flux_mcdc == 0.0
zero_openmc = flux_openmc == 0.0
reference = 0.5 * (flux_mcdc + flux_openmc)
reference[zero_mcdc] = flux_openmc[zero_mcdc]
reference[zero_openmc] = flux_mcdc[zero_openmc]
non_zeros = reference != 0.0
reference = reference[non_zeros]

for n in range(NN):
    # Get results
    with h5py.File("mcdc/output_%i.h5" % n, "r") as f:
        flux_mcdc = f["tallies/tracklength_tally_0/flux/mean"][()]

    # Get results
    with openmc.StatePoint("openmc_/output_%i.h5" % n) as sp:
        tally = sp.get_tally(scores=["flux"])
        flux_openmc = tally.mean.reshape((100, 60, 100, 60))
        flux_openmc = np.swapaxes(flux_openmc, 1, 3)

    difference[n] = np.linalg.norm(
        (flux_mcdc[non_zeros] - flux_openmc[non_zeros]) / reference
    )

plt.plot(N_list, difference, "bo", fillstyle="none")

mid = int(len(N_list) / 2)
line = 1.0 / np.sqrt(N_list)
line *= difference[mid] / line[mid]
plt.plot(N_list, line, "r--", label=r"$O(N^{-0.5})$")

plt.xscale("log")
plt.yscale("log")
plt.ylabel("2-norm of relative difference")
plt.xlabel(r"# of histories, $N$")
plt.grid()
plt.legend()
plt.title("Convergence of MC/DC and OpenMC relative difference")
plt.savefig(f"convergence.png", dpi=300, bbox_inches="tight", pad_inches=0)
plt.show()
