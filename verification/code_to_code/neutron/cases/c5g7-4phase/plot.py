"""Animate one C5G7 MC/DC and OpenMC result pair."""

import argparse

import h5py
import numpy as np

from process import load_mcdc_fission, load_openmc_fission
from util import (
    animate_spatial_comparison,
    animate_spatial_difference,
    comparison_reference,
    relative_difference,
)

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
    x = f["tallies/tracklength_tally_0/grid/x"][:]
    y = f["tallies/tracklength_tally_0/grid/y"][:]
    z = f["tallies/tracklength_tally_0/grid/z"][:]

fission_openmc = load_openmc_fission(args.openmc_output)
time_mid = 0.5 * (time[:-1] + time[1:])

animate_spatial_comparison(
    "fission",
    time_mid,
    (x, y, z),
    fission_mcdc,
    fission_openmc,
    "MC/DC",
    "OpenMC",
)

rms_difference = np.empty(len(time_mid))
for index in range(len(time_mid)):
    difference = relative_difference(
        reference[index],
        fission_mcdc[index],
        fission_openmc[index],
    )
    rms_difference[index] = np.sqrt(np.mean(np.square(difference)))

animate_spatial_difference(
    "fission",
    time_mid,
    (x, y, z),
    reference,
    fission_mcdc,
    fission_openmc,
    rms_difference,
    "RMS relative difference (%)",
)
