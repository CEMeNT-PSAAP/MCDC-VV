"""Plot neutron spectra sampled in the integral FNG SiC model."""

import argparse

import h5py
import matplotlib.pyplot as plt
import numpy as np

POSITION_LABELS = {
    "activation": [10.41, 25.65, 40.89, 56.13],
    "heating": [14.99, 30.23, 45.47, 60.71],
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


# Separate the activation and heating locations because they correspond to
# different experimental responses in the official benchmark.
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.5), sharex=True, sharey=True)
with h5py.File(args.input, "r") as output:
    for ax, (kind, positions) in zip(axes, POSITION_LABELS.items()):
        for index, position in enumerate(positions, start=1):
            energy, spectrum, spectrum_sdev = read_spectrum(
                output, f"{kind}_flux_p{index}"
            )
            (line,) = ax.step(
                energy,
                spectrum,
                where="mid",
                label=f"P{index}: {position:.2f} cm",
            )
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
        ax.set_title(f"{kind.capitalize()} positions")
        ax.grid(which="both", alpha=0.25)
        ax.legend()

axes[0].set_ylabel(r"Neutron flux [source$^{-1}$ cm$^{-2}$ MeV$^{-1}$]")
fig.suptitle("FNG SiC public-entry model")
fig.tight_layout()
fig.savefig(args.output, dpi=200)
plt.close(fig)
