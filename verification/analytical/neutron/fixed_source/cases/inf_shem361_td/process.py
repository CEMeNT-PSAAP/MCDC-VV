from pathlib import Path

import numpy as np
import h5py
import sys

SHEM361_DATA = Path(__file__).resolve().parents[2] / "data" / "SHEM-361.npz"

sys.path.append("../../")
import util

# Particle counts
N_min = int(sys.argv[1])
N_max = int(sys.argv[2])
N = int(sys.argv[3])
N_particle_list = np.logspace(N_min, N_max, N, dtype=int)

# Reference solution
data = np.load("reference.npz")
phi_ref_ = data["phi"].T
n_ref = data["n"].T

# Error container
error = np.zeros(len(N_particle_list))
error_n = np.zeros(len(N_particle_list))

error_max = np.zeros(len(N_particle_list))
error_max_n = np.zeros(len(N_particle_list))

# Calculate error
for i, N_particle in enumerate(N_particle_list):
    # Get results
    with np.load(SHEM361_DATA) as data:
        E = data["E"]
        speed = data["v"]
        E_mid = 0.5 * (E[1:] + E[:-1])
        dE = E[1:] - E[:-1]
    with h5py.File("output_%i.h5" % (int(N_particle)), "r") as f:
        t = f["tallies/tracklength_tally_0/grid/time"][:]
        dt = t[1:] - t[:-1]
        K = len(t) - 1
        phi = f["tallies/tracklength_tally_0/flux/mean"][:]

    # Neutron density
    n = np.zeros(K)
    for k in range(K):
        n[k] = np.sum(phi[:, k] / speed) / dt[k]

    # Normalize
    phi_ref = np.zeros_like(phi_ref_)
    for k in range(K):
        phi_ref[:, k] = phi_ref_[:, k] * E_mid / dE
        phi[:, k] *= E_mid / dE / dt[k]

    error[i] = util.rerror(phi, phi_ref)
    error_n[i] = util.rerror(n, n_ref)
    error_max[i] = util.rerror_max(phi, phi_ref)
    error_max_n[i] = util.rerror_max(n, n_ref)

util.plot_convergence("flux", N_particle_list, error, error_max)
util.plot_convergence("n", N_particle_list, error_n, error_max_n)
