"""Measure convergence against the analytical manufactured solution."""

import subprocess
import sys
from pathlib import Path

import h5py
import numpy as np

from reference import cell_average_scalar_flux

SUITE_DIR = Path(__file__).resolve().parents[2]
if str(SUITE_DIR) not in sys.path:
    sys.path.insert(0, str(SUITE_DIR))

import util

logN_min = int(sys.argv[1])
logN_max = int(sys.argv[2])
N_task = int(sys.argv[3])
particle_counts = np.logspace(logN_min, logN_max, N_task, dtype=int)

error = np.zeros(N_task)
error_max = np.zeros(N_task)

for index, N_particle in enumerate(particle_counts):
    with h5py.File(f"output_{N_particle}.h5", "r") as output:
        x = output["tallies/tracklength_tally_0/grid/x"][:]
        dx = np.diff(x)
        flux = output["tallies/tracklength_tally_0/flux/mean"][:]

    flux = flux / dx
    reference = cell_average_scalar_flux(x)
    error[index] = util.rerror(flux, reference)
    error_max[index] = util.rerror_max(flux, reference)

util.plot_convergence("flux", particle_counts, error, error_max)

# Include a detailed comparison for the highest-statistics result.
subprocess.run(
    [sys.executable, "plot.py", f"output_{particle_counts[-1]}.h5"],
    check=True,
)
