"""Process the C5G7 particle-count study with archived OpenMC results."""

import argparse
import sys
from pathlib import Path

import h5py
import numpy as np

SUITE_DIR = Path(__file__).resolve().parents[2]
if str(SUITE_DIR) not in sys.path:
    sys.path.insert(0, str(SUITE_DIR))

from util import (
    comparison_reference,
    load_openmc_tally,
    particle_counts,
    plot_convergence,
    relative_difference_metrics,
    require_reference_files,
)

N_TIME = 200
N_X = 17 * 2
N_Y = 17 * 2
N_Z = 17 * 6


def load_mcdc_fission(path):
    """Load the MC/DC space-time fission mesh and batch count."""
    with h5py.File(path, "r") as f:
        fission = f["tallies/tracklength_tally_0/fission/mean"][:]
        N_batch = int(f["settings/N_batch"][()])
    return fission, N_batch


def load_openmc_fission(path):
    """Load the OpenMC space-time fission mesh in MC/DC axis order."""
    fission = load_openmc_tally(path, "pincell fission").reshape(
        (N_TIME, N_Z, N_Y, N_X)
    )
    return np.swapaxes(fission, 1, 3)


def main():
    """Process every particle-count task and generate the convergence figure."""
    parser = argparse.ArgumentParser()
    parser.add_argument("logN_min", type=float)
    parser.add_argument("logN_max", type=float)
    parser.add_argument("N_task", type=int)
    args = parser.parse_args()

    case_dir = Path(__file__).resolve().parent
    N_particle = particle_counts(args.logN_min, args.logN_max, args.N_task)
    reference_files = require_reference_files(case_dir, args.N_task)
    difference_l2 = np.zeros(args.N_task)
    difference_max = np.zeros(args.N_task)

    mcdc_reference, N_batch = load_mcdc_fission(
        case_dir / f"output_{int(N_particle[-1])}.h5"
    )
    openmc_reference = load_openmc_fission(reference_files[-1])
    reference = comparison_reference(mcdc_reference, openmc_reference)
    del mcdc_reference, openmc_reference

    for index, (count, reference_file) in enumerate(zip(N_particle, reference_files)):
        mcdc_fission, current_N_batch = load_mcdc_fission(
            case_dir / f"output_{int(count)}.h5"
        )
        openmc_fission = load_openmc_fission(reference_file)
        difference_l2[index], difference_max[index] = relative_difference_metrics(
            reference,
            mcdc_fission,
            openmc_fission,
        )

        if current_N_batch != N_batch:
            raise ValueError("All MC/DC outputs must use the same number of batches.")

    plot_convergence(
        "fission",
        N_particle * N_batch,
        difference_l2,
        difference_max,
    )


if __name__ == "__main__":
    main()
