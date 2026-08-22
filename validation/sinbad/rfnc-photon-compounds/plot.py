"""Plot the RFNC precursor's diagnostic neutron leakage spectrum."""

import argparse

import h5py
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("input", nargs="?", default="output.h5")
parser.add_argument("--output", default="neutron-leakage-diagnostic.png")
args = parser.parse_args()

# Load the diagnostic neutron current and convert it to a differential spectrum.
with h5py.File(args.input, "r") as output:
    tally = output["tallies/neutron_leakage_diagnostic"]
    energy = tally["grid/energy"][:]
    current = np.asarray(tally["current-out/mean"][:]).squeeze()
    current_sdev = np.asarray(tally["current-out/sdev"][:]).squeeze()

energy_midpoint = np.sqrt(energy[:-1] * energy[1:]) * 1.0e-6
energy_width = np.diff(energy) * 1.0e-6
spectrum = current / energy_width
spectrum_sdev = current_sdev / energy_width

# Label the figure as an intermediate diagnostic to avoid confusing it with the
# measured photon-leakage spectrum.
fig, ax = plt.subplots(figsize=(7.0, 4.5))
ax.step(energy_midpoint, spectrum, where="mid", color="tab:blue", label="MC/DC")
ax.fill_between(
    energy_midpoint,
    np.maximum(spectrum - spectrum_sdev, np.finfo(float).tiny),
    spectrum + spectrum_sdev,
    step="mid",
    color="tab:blue",
    alpha=0.25,
    linewidth=0.0,
    label=r"MC standard deviation",
)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Neutron energy [MeV]")
ax.set_ylabel(r"Outward neutron current [source$^{-1}$ MeV$^{-1}$]")
ax.set_title("RFNC compound model: neutron precursor diagnostic")
ax.grid(which="both", alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig(args.output, dpi=200)
plt.close(fig)
