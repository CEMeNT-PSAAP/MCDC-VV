from reference import reference
import numpy as np
import h5py
import sys

sys.path.append("../../")
import util

# Particle counts
N_min = int(sys.argv[1])
N_max = int(sys.argv[2])
N = int(sys.argv[3])
N_particle_list = np.logspace(N_min, N_max, N, dtype=int)

# Reference solution
phi_ref = reference()

# Error container
error = np.zeros(len(N_particle_list))
error_max = np.zeros(len(N_particle_list))

# Calculate error
for k, N_particle in enumerate(N_particle_list):
    # Get results
    with h5py.File("output_%i.h5" % (int(N_particle)), "r") as f:
        phi = f["tallies/tracklength_tally_0/flux/mean"][:]

    error[k] = util.rerror(phi, phi_ref)
    error_max[k] = util.rerror_max(phi, phi_ref)

# Plot
util.plot_convergence("flux", N_particle_list, error, error_max)
