"""Shared processing helpers for neutron code-to-code cases."""

from pathlib import Path

import h5py
import matplotlib.pyplot as plt
import numpy as np


def particle_counts(logN_min, logN_max, N_task):
    """Return logarithmically spaced particles per batch for a case study."""
    return np.logspace(logN_min, logN_max, N_task, dtype=int)


def require_reference_files(case_dir, N_task):
    """Return the expected reference files or explain how to obtain them."""
    reference_files = [
        case_dir / "reference" / f"output_{index}.h5" for index in range(N_task)
    ]
    missing = [path for path in reference_files if not path.is_file()]

    if missing:
        raise FileNotFoundError(
            f"Missing {len(missing)} reference output(s) for {case_dir.name}. "
            f"Run: python {case_dir / 'reference.py'}"
        )

    return reference_files


def load_openmc_tally(path, name):
    """Load a named tally mean directly from an OpenMC statepoint."""
    with h5py.File(path, "r") as statepoint:
        tallies = statepoint["tallies"]

        for key, tally in tallies.items():
            if not key.startswith("tally ") or "name" not in tally:
                continue

            tally_name = tally["name"][()]
            if isinstance(tally_name, bytes):
                tally_name = tally_name.decode()

            if tally_name != name:
                continue

            N_realization = int(tally["n_realizations"][()])
            tally_sum = tally["results"][..., 0]
            return np.asarray(tally_sum).reshape(-1) / N_realization

    raise KeyError(f"OpenMC tally '{name}' not found in {path}")


def comparison_reference(*results):
    """Return the arithmetic mean of the participating code estimates."""
    if len(results) < 2:
        raise ValueError("At least two code estimates are required.")

    results = tuple(np.asarray(result) for result in results)
    if any(result.shape != results[0].shape for result in results[1:]):
        raise ValueError("All code estimates must have the same shape.")

    dtype = np.result_type(*(result.dtype for result in results), np.float64)
    reference = np.zeros_like(results[0], dtype=dtype)
    for result in results:
        reference += result
    return reference / len(results)


def relative_difference_l2(reference, *results):
    """Return the pair-averaged L2 norm against a fixed comparison reference."""
    reference = np.asarray(reference)
    results = tuple(np.asarray(result) for result in results)

    if len(results) < 2:
        raise ValueError("At least two code estimates are required.")
    if any(result.shape != reference.shape for result in results):
        raise ValueError("The reference and code estimates must have the same shape.")

    nonzero = np.abs(reference) > 0.0

    if not np.any(nonzero):
        return 0.0

    squared_norms = []
    for first in range(len(results) - 1):
        for second in range(first + 1, len(results)):
            relative_difference = (
                results[first][nonzero] - results[second][nonzero]
            ) / reference[nonzero]
            squared_norms.append(np.linalg.norm(relative_difference) ** 2)

    return np.sqrt(np.mean(squared_norms))


def plot_convergence(score, N_history, difference):
    """Plot code-to-code difference alongside the Monte Carlo convergence rate."""
    N_history = np.asarray(N_history)
    difference = np.asarray(difference)

    fig, ax = plt.subplots()
    ax.plot(
        N_history,
        difference,
        "bo",
        fillstyle="none",
        label="Code-to-code difference",
    )

    positive = difference > 0.0
    if np.any(positive):
        anchor = np.flatnonzero(positive)[len(np.flatnonzero(positive)) // 2]
        expected = 1.0 / np.sqrt(N_history)
        expected *= difference[anchor] / expected[anchor]
        ax.plot(N_history, expected, "r--", label=r"$O(N^{-1/2})$")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"Number of particle histories, $N$")
    ax.set_ylabel("L2 norm of relative difference")
    ax.set_title(f"{score.capitalize()} convergence")
    ax.grid()
    ax.legend()
    fig.savefig(
        Path(f"convergence_{score}.png"),
        dpi=300,
        bbox_inches="tight",
        pad_inches=0,
    )
    plt.close(fig)
