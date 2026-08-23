"""Measure active-cycle convergence against the Kornreich reference."""

import sys
from pathlib import Path

import h5py
import numpy as np

from reference import reference

SUITE_DIR = Path(__file__).resolve().parents[2]
if str(SUITE_DIR) not in sys.path:
    sys.path.insert(0, str(SUITE_DIR))

import util

N_active_min = int(sys.argv[1])
N_active_max = int(sys.argv[2])
N_task = int(sys.argv[3])
active_cycle_counts = np.rint(
    np.geomspace(
        N_active_min,
        N_active_max,
        N_task,
    )
).astype(int)

k_error = np.zeros(N_task)
k_estimate = np.zeros(N_task)
k_uncertainty = np.zeros(N_task)
flux_error = np.zeros(N_task)

# Calculate the semi-analytical flux once and use the published multiplication factor.
with h5py.File(f"output_{active_cycle_counts[0]}.h5", "r") as output:
    x_reference = output["tallies/tracklength_tally_0/grid/x"][:]
k_reference, flux_reference = reference(x_reference)

for index, N_active in enumerate(active_cycle_counts):
    with h5py.File(f"output_{N_active}.h5", "r") as output:
        k_estimate[index] = output["k_mean"][()]
        k_uncertainty[index] = output["k_sdev"][()]
        x = output["tallies/tracklength_tally_0/grid/x"][:]
        dx = np.diff(x)
        flux = output["tallies/tracklength_tally_0/flux/mean"][:] / dx

    # Eigenvectors have arbitrary amplitude, so compare unit-integral shapes.
    flux /= np.sum(flux * dx)
    k_error[index] = abs(k_estimate[index] - k_reference) / k_reference
    flux_error[index] = util.relative_error(flux, flux_reference)

util.plot_convergence("k-effective", active_cycle_counts, k_error)
util.plot_k_estimates(
    active_cycle_counts,
    k_estimate,
    k_uncertainty,
    k_reference,
)
util.plot_convergence("flux", active_cycle_counts, flux_error)
