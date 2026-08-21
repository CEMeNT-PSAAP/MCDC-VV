"""Inspect one Kobayashi MC/DC and OpenMC result pair."""

import argparse

import h5py
import matplotlib.pyplot as plt
import numpy as np

from process import load_mcdc_results, load_openmc_results
from util import comparison_reference

parser = argparse.ArgumentParser()
parser.add_argument("mcdc_output")
parser.add_argument("openmc_output")
parser.add_argument("mcdc_reference_output")
parser.add_argument("openmc_reference_output")
args = parser.parse_args()

mcdc_flux_reference, mcdc_density_reference, _ = load_mcdc_results(
    args.mcdc_reference_output
)
openmc_flux_reference, openmc_density_reference = load_openmc_results(
    args.openmc_reference_output
)
reference = comparison_reference(mcdc_flux_reference, openmc_flux_reference)
del (
    mcdc_flux_reference,
    mcdc_density_reference,
    openmc_flux_reference,
    openmc_density_reference,
)

with h5py.File(args.mcdc_output, "r") as f:
    flux_mcdc = f["tallies/tracklength_tally_0/flux/mean"][:]
    density_mcdc = f["tallies/tracklength_tally_1/density/mean"][:]
    time = f["tallies/tracklength_tally_0/grid/time"][:]

flux_openmc, density_openmc = load_openmc_results(args.openmc_output)
time_mid = 0.5 * (time[:-1] + time[1:])

relative_difference = np.zeros_like(reference)
nonzero = np.abs(reference) > 0.0
relative_difference[nonzero] = (flux_mcdc[nonzero] - flux_openmc[nonzero]) / reference[
    nonzero
]
rms_difference = np.sqrt(np.mean(np.square(relative_difference), axis=(1, 2, 3)))

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(time_mid, density_mcdc, "b", label="MC/DC")
axes[0].plot(time_mid, density_openmc, "r--", label="OpenMC")
axes[0].set_yscale("log")
axes[0].set_ylabel("Neutron density")
axes[0].grid()
axes[0].legend()

axes[1].plot(time_mid, rms_difference, "k")
axes[1].set_yscale("log")
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Flux RMS relative difference")
axes[1].grid()

fig.suptitle("Time-dependent Kobayashi dog-leg")
fig.savefig("comparison.png", dpi=200, bbox_inches="tight")
plt.close(fig)
