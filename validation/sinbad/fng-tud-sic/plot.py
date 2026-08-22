"""Plot neutron spectra for the FNG/TUD SiC public-entry model."""

import argparse

import h5py
import matplotlib.pyplot as plt
import numpy as np

POSITIONS = {
    "p1": "P1: 12.70 cm",
    "p2": "P2: 27.94 cm",
    "p3": "P3: 43.18 cm",
    "p4": "P4: 58.42 cm",
}

parser = argparse.ArgumentParser()
parser.add_argument("input", nargs="?", default="output.h5")
parser.add_argument("--output", default="neutron-spectra.png")
args = parser.parse_args()


def read_spectrum(output, name):
    """Return a volume- and energy-differential neutron flux spectrum."""
    tally = output[f"tallies/{name}"]
    energy = tally["grid/energy"][:]
    volume = np.prod(
        [
            np.diff(tally["grid/x"])[0],
            np.diff(tally["grid/y"])[0],
            np.diff(tally["grid/z"])[0],
        ]
    )
    energy_width = np.diff(energy) * 1.0e-6
    mean = np.asarray(tally["flux/mean"][:]).squeeze() / volume / energy_width
    sdev = np.asarray(tally["flux/sdev"][:]).squeeze() / volume / energy_width
    return np.sqrt(energy[:-1] * energy[1:]) * 1.0e-6, mean, sdev


# Plot the four calculated neutron spectra without an experimental overlay.
fig, ax = plt.subplots(figsize=(7.0, 4.5))
with h5py.File(args.input, "r") as output:
    for label, description in POSITIONS.items():
        energy, spectrum, spectrum_sdev = read_spectrum(output, f"neutron_flux_{label}")
        (line,) = ax.step(energy, spectrum, where="mid", label=description)
        ax.fill_between(
            energy,
            np.maximum(spectrum - spectrum_sdev, np.finfo(float).tiny),
            spectrum + spectrum_sdev,
            step="mid",
            color=line.get_color(),
            alpha=0.12,
            linewidth=0.0,
        )

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Neutron energy [MeV]")
ax.set_ylabel(r"Neutron flux [source$^{-1}$ cm$^{-2}$ MeV$^{-1}$]")
ax.set_title("FNG/TUD SiC public-entry model")
ax.grid(which="both", alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig(args.output, dpi=200)
plt.close(fig)
