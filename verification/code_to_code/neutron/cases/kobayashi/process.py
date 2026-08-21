"""Process the Kobayashi particle-count study with archived OpenMC results."""

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
    relative_difference_l2,
    require_reference_files,
)

N_TIME = 100
N_X = 60
N_Y = 100
N_Z = 60


def load_mcdc_results(path):
    """Load the MC/DC flux, density, and batch count."""
    with h5py.File(path, "r") as f:
        flux = f["tallies/tracklength_tally_0/flux/mean"][:]
        density = f["tallies/tracklength_tally_1/density/mean"][:]
        N_batch = int(f["settings/N_batch"][()])
    return flux, density, N_batch


def load_openmc_results(path):
    """Load the OpenMC flux and density in MC/DC axis order."""
    flux = load_openmc_tally(path, "flux").reshape((N_TIME, N_Z, N_Y, N_X))
    density = load_openmc_tally(path, "density").reshape(N_TIME)
    return np.swapaxes(flux, 1, 3), density


def main():
    """Process every particle-count task and generate the convergence figures."""
    parser = argparse.ArgumentParser()
    parser.add_argument("logN_min", type=float)
    parser.add_argument("logN_max", type=float)
    parser.add_argument("N_task", type=int)
    args = parser.parse_args()

    case_dir = Path(__file__).resolve().parent
    N_particle = particle_counts(args.logN_min, args.logN_max, args.N_task)
    reference_files = require_reference_files(case_dir, args.N_task)
    flux_difference = np.zeros(args.N_task)
    density_difference = np.zeros(args.N_task)

    mcdc_flux_reference, mcdc_density_reference, N_batch = load_mcdc_results(
        case_dir / f"output_{int(N_particle[-1])}.h5"
    )
    openmc_flux_reference, openmc_density_reference = load_openmc_results(
        reference_files[-1]
    )
    flux_reference = comparison_reference(
        mcdc_flux_reference,
        openmc_flux_reference,
    )
    density_reference = comparison_reference(
        mcdc_density_reference,
        openmc_density_reference,
    )
    del (
        mcdc_flux_reference,
        mcdc_density_reference,
        openmc_flux_reference,
        openmc_density_reference,
    )

    for index, (count, reference_file) in enumerate(zip(N_particle, reference_files)):
        mcdc_flux, mcdc_density, current_N_batch = load_mcdc_results(
            case_dir / f"output_{int(count)}.h5"
        )
        openmc_flux, openmc_density = load_openmc_results(reference_file)
        flux_difference[index] = relative_difference_l2(
            flux_reference,
            mcdc_flux,
            openmc_flux,
        )
        density_difference[index] = relative_difference_l2(
            density_reference,
            mcdc_density,
            openmc_density,
        )

        if current_N_batch != N_batch:
            raise ValueError("All MC/DC outputs must use the same number of batches.")

    N_history = N_particle * N_batch
    plot_convergence("flux", N_history, flux_difference)
    plot_convergence("density", N_history, density_difference)


if __name__ == "__main__":
    main()
