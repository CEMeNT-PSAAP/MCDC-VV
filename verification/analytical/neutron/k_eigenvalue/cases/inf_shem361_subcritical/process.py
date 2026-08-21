import sys
from pathlib import Path

import h5py
import numpy as np

from reference import reference

SUITE_DIR = Path(__file__).resolve().parents[2]
if str(SUITE_DIR) not in sys.path:
    sys.path.insert(0, str(SUITE_DIR))

import util

# Reproduce the active-cycle counts used by run_case.py.
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

# Calculate the dominant analytical eigenpair once for all tasks.
k_reference, flux_reference = reference()
k_error = np.zeros(N_task)
k_estimate = np.zeros(N_task)
k_uncertainty = np.zeros(N_task)
flux_error = np.zeros(N_task)

for index, N_active in enumerate(active_cycle_counts):
    with h5py.File(f"output_{N_active}.h5", "r") as output:
        k_estimate[index] = output["k_mean"][()]
        k_uncertainty[index] = output["k_sdev"][()]
        flux = output["tallies/tracklength_tally_0/flux/mean"][:]

    # Only the spectrum shape matters for this infinite-medium eigenproblem.
    flux /= np.sum(flux)
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
