"""Animate one Kobayashi MC/DC and OpenMC result pair."""

import argparse

import h5py
import numpy as np

from process import load_mcdc_results, load_openmc_results
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

mcdc_flux_reference, mcdc_density_reference, _ = load_mcdc_results(
    args.mcdc_reference_output
)
openmc_flux_reference, openmc_density_reference = load_openmc_results(
    args.openmc_reference_output
)
reference = comparison_reference(mcdc_flux_reference, openmc_flux_reference)
reference_density = comparison_reference(
    mcdc_density_reference,
    openmc_density_reference,
)
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
    x = f["tallies/tracklength_tally_0/grid/x"][:]
    y = f["tallies/tracklength_tally_0/grid/y"][:]
    z = f["tallies/tracklength_tally_0/grid/z"][:]

flux_openmc, density_openmc = load_openmc_results(args.openmc_output)
time_mid = 0.5 * (time[:-1] + time[1:])

animate_spatial_comparison(
    "flux",
    time_mid,
    (x, y, z),
    flux_mcdc,
    flux_openmc,
    "MC/DC",
    "OpenMC",
)

density_difference = np.abs(
    relative_difference(reference_density, density_mcdc, density_openmc)
)
animate_spatial_difference(
    "flux",
    time_mid,
    (x, y, z),
    reference,
    flux_mcdc,
    flux_openmc,
    density_difference,
    "Density relative difference (%)",
)
