import h5py
import matplotlib.pyplot as plt
import numpy as np
import openmc
import os
import shutil

N_list = np.array([100000, 316227, 1000000, 3162277, 10000000]) * 30

NN = len(N_list)

Nt = 200
Nx = 17 * 2
Ny = 17 * 2
Nz = 17 * 6

difference = np.zeros(NN)

# Getting the reference
with h5py.File("mcdc/output_4.h5", "r") as f:
    fission_mcdc = f["tallies/tracklength_tally_0/fission/mean"][()]

with openmc.StatePoint("openmc_/output_4.h5") as sp:
    tally = sp.get_tally(name="pincell fission")
    fission_openmc = tally.mean.reshape((Nt, Nz, Ny, Nx))
    fission_openmc = np.swapaxes(fission_openmc, 1, 3)

zero_mcdc = fission_mcdc == 0.0
zero_openmc = fission_openmc == 0.0
reference = 0.5 * (fission_mcdc + fission_openmc)
reference[zero_mcdc] = fission_openmc[zero_mcdc]
reference[zero_openmc] = fission_mcdc[zero_openmc]
non_zeros = reference != 0.0
reference = reference[non_zeros]

for n in range(NN):
    # Get results
    with h5py.File("mcdc/output_%i.h5" % n, "r") as f:
        fission_mcdc = f["tallies/tracklength_tally_0/fission/mean"][()]

    # Get results
    with openmc.StatePoint("openmc_/output_%i.h5" % n) as sp:
        tally = sp.get_tally(name="pincell fission")
        fission_openmc = tally.mean.reshape((Nt, Nz, Ny, Nx))
        fission_openmc = np.swapaxes(fission_openmc, 1, 3)

    difference[n] = np.linalg.norm(
        (fission_mcdc[non_zeros] - fission_openmc[non_zeros]) / reference
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
