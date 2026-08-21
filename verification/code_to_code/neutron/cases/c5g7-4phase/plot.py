"""Inspect one C5G7 MC/DC and OpenMC result pair."""

import argparse

import h5py
import matplotlib.pyplot as plt
import numpy as np

from process import load_mcdc_fission, load_openmc_fission
from util import comparison_reference

parser = argparse.ArgumentParser()
parser.add_argument("mcdc_output")
parser.add_argument("openmc_output")
parser.add_argument("mcdc_reference_output")
parser.add_argument("openmc_reference_output")
args = parser.parse_args()

mcdc_reference, _ = load_mcdc_fission(args.mcdc_reference_output)
openmc_reference = load_openmc_fission(args.openmc_reference_output)
reference = comparison_reference(mcdc_reference, openmc_reference)
del mcdc_reference, openmc_reference

with h5py.File(args.mcdc_output, "r") as f:
    fission_mcdc = f["tallies/tracklength_tally_0/fission/mean"][:]
    time = f["tallies/tracklength_tally_0/grid/time"][:]

fission_openmc = load_openmc_fission(args.openmc_output)
time_mid = 0.5 * (time[:-1] + time[1:])

fission_total_mcdc = np.sum(fission_mcdc, axis=(1, 2, 3))
fission_total_openmc = np.sum(fission_openmc, axis=(1, 2, 3))

relative_difference = np.zeros_like(reference)
nonzero = np.abs(reference) > 0.0
relative_difference[nonzero] = (
    fission_mcdc[nonzero] - fission_openmc[nonzero]
) / reference[nonzero]
rms_difference = np.sqrt(np.mean(np.square(relative_difference), axis=(1, 2, 3)))

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(time_mid, fission_total_mcdc, "b", label="MC/DC")
axes[0].plot(time_mid, fission_total_openmc, "r--", label="OpenMC")
axes[0].set_yscale("log")
axes[0].set_ylabel("Total fission rate")
axes[0].grid()
axes[0].legend()

axes[1].plot(time_mid, rms_difference, "k")
axes[1].set_yscale("log")
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("RMS relative difference")
axes[1].grid()

fig.suptitle("Four-phase C5G7 transient")
plt.show()
