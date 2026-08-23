"""Shared processing helpers for neutron code-to-code cases."""

from pathlib import Path

import h5py
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm, Normalize


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


def relative_difference(reference, first, second):
    """Return the pointwise difference between two codes relative to a reference."""
    reference = np.asarray(reference)
    first = np.asarray(first)
    second = np.asarray(second)

    if first.shape != reference.shape or second.shape != reference.shape:
        raise ValueError("The reference and code estimates must have the same shape.")

    difference = np.zeros_like(reference, dtype=np.float64)
    nonzero = np.abs(reference) > 0.0
    difference[nonzero] = (first[nonzero] - second[nonzero]) / reference[nonzero]
    return difference


def relative_difference_metrics(reference, *results):
    """Return pairwise L2 and maximum differences against a fixed reference."""
    reference = np.asarray(reference)
    results = tuple(np.asarray(result) for result in results)

    if len(results) < 2:
        raise ValueError("At least two code estimates are required.")
    if any(result.shape != reference.shape for result in results):
        raise ValueError("The reference and code estimates must have the same shape.")

    nonzero = np.abs(reference) > 0.0

    if not np.any(nonzero):
        return 0.0, 0.0

    squared_norms = []
    maximum = 0.0
    for first in range(len(results) - 1):
        for second in range(first + 1, len(results)):
            difference = (
                results[first][nonzero] - results[second][nonzero]
            ) / reference[nonzero]
            squared_norms.append(np.linalg.norm(difference) ** 2)
            maximum = max(maximum, float(np.max(np.abs(difference))))

    return np.sqrt(np.mean(squared_norms)), maximum


def relative_difference_l2(reference, *results):
    """Return the pair-averaged L2 norm against a fixed comparison reference."""
    return relative_difference_metrics(reference, *results)[0]


def relative_difference_max(reference, *results):
    """Return the maximum absolute pairwise difference against a fixed reference."""
    return relative_difference_metrics(reference, *results)[1]


def _spatial_projections(result):
    """Integrate a time-dependent 3D field into its three planar projections."""
    result = np.asarray(result)
    if result.ndim != 4:
        raise ValueError("A space-time result must have shape (time, x, y, z).")

    return (
        np.sum(result, axis=3),
        np.sum(result, axis=2),
        np.sum(result, axis=1),
    )


def _positive_norm(*results):
    """Return a shared logarithmic scale for nonnegative code estimates."""
    maximum = max(float(np.nanmax(result)) for result in results)
    if maximum <= 0.0:
        return Normalize(vmin=0.0, vmax=1.0)

    minima = [
        float(np.nanmin(result[result > 0.0]))
        for result in results
        if np.any(result > 0.0)
    ]
    minimum = max(min(minima), maximum * 1.0e-6)
    if minimum >= maximum:
        minimum = 0.5 * maximum
    return LogNorm(vmin=minimum, vmax=maximum)


def animate_spatial_comparison(
    score,
    time,
    spatial_edges,
    first,
    second,
    first_label,
    second_label,
    filename="comparison.gif",
):
    """Animate orthogonal projections of two participating-code estimates."""
    time = np.asarray(time)
    x, y, z = (np.asarray(edges) for edges in spatial_edges)
    first_projections = _spatial_projections(first)
    second_projections = _spatial_projections(second)
    projection_data = (
        ("XY", x, y, first_projections[0], second_projections[0]),
        ("XZ", x, z, first_projections[1], second_projections[1]),
        ("YZ", y, z, first_projections[2], second_projections[2]),
    )

    fig, axes = plt.subplots(2, 3, figsize=(12, 7), constrained_layout=True)
    images = []
    for column, (plane, horizontal, vertical, first_data, second_data) in enumerate(
        projection_data
    ):
        norm = _positive_norm(first_data, second_data)
        first_image = axes[0, column].imshow(
            first_data[0].T,
            extent=(horizontal[0], horizontal[-1], vertical[0], vertical[-1]),
            origin="lower",
            aspect="auto",
            cmap="viridis",
            norm=norm,
        )
        second_image = axes[1, column].imshow(
            second_data[0].T,
            extent=(horizontal[0], horizontal[-1], vertical[0], vertical[-1]),
            origin="lower",
            aspect="auto",
            cmap="viridis",
            norm=norm,
        )
        axes[0, column].set_title(f"{first_label} {plane}")
        axes[1, column].set_title(f"{second_label} {plane}")
        axes[1, column].set_xlabel(plane[0].lower())
        axes[0, column].set_ylabel(plane[1].lower())
        axes[1, column].set_ylabel(plane[1].lower())
        fig.colorbar(first_image, ax=axes[:, column], label=score.capitalize())
        images.append((first_image, second_image, first_data, second_data))

    title = fig.suptitle(f"{score.capitalize()} comparison, t = {time[0]:.3g}")

    def update(frame):
        for first_image, second_image, first_data, second_data in images:
            first_image.set_data(first_data[frame].T)
            second_image.set_data(second_data[frame].T)
        title.set_text(f"{score.capitalize()} comparison, t = {time[frame]:.3g}")
        return [title, *(image for pair in images for image in pair[:2])]

    simulation = animation.FuncAnimation(fig, update, frames=len(time))
    simulation.save(
        filename,
        writer=animation.PillowWriter(fps=max(2, len(time) // 10)),
        dpi=120,
    )
    plt.close(fig)


def animate_spatial_difference(
    score,
    time,
    spatial_edges,
    reference,
    first,
    second,
    metric,
    metric_label,
    filename="difference.gif",
):
    """Animate the history and spatial projections of code-to-code differences."""
    time = np.asarray(time)
    metric = 100.0 * np.asarray(metric)
    x, y, z = (np.asarray(edges) for edges in spatial_edges)

    reference_projections = _spatial_projections(reference)
    first_projections = _spatial_projections(first)
    second_projections = _spatial_projections(second)
    differences = tuple(
        100.0 * relative_difference(current_reference, current_first, current_second)
        for current_reference, current_first, current_second in zip(
            reference_projections,
            first_projections,
            second_projections,
        )
    )
    projection_data = (
        ("XY", x, y, differences[0]),
        ("XZ", x, z, differences[1]),
        ("YZ", y, z, differences[2]),
    )

    percentiles = [
        float(np.nanpercentile(np.abs(difference), 99.0)) for difference in differences
    ]
    color_limit = min(100.0, max(1.0, *percentiles))
    norm = Normalize(vmin=-color_limit, vmax=color_limit)

    fig, axes = plt.subplots(2, 2, figsize=(12, 9), constrained_layout=True)
    metric_axis = axes[0, 0]
    positive_metric = np.where(metric > 0.0, metric, np.nan)
    metric_axis.plot(time, positive_metric, "b")
    marker = metric_axis.plot([], [], "ro", fillstyle="none")[0]
    if np.any(metric > 0.0):
        metric_axis.set_yscale("log")
    metric_axis.set_xlabel("Time")
    metric_axis.set_ylabel(metric_label)
    metric_axis.grid()

    images = []
    for axis, (plane, horizontal, vertical, difference) in zip(
        (axes[0, 1], axes[1, 0], axes[1, 1]), projection_data
    ):
        image = axis.imshow(
            difference[0].T,
            extent=(horizontal[0], horizontal[-1], vertical[0], vertical[-1]),
            origin="lower",
            aspect="auto",
            cmap="RdBu_r",
            norm=norm,
        )
        axis.set_title(f"{score.capitalize()}-{plane}")
        axis.set_xlabel(plane[0].lower())
        axis.set_ylabel(plane[1].lower())
        images.append((image, difference))

    fig.colorbar(
        images[0][0],
        ax=(axes[0, 1], axes[1, 0], axes[1, 1]),
        label="Relative difference (%)",
    )
    title = fig.suptitle(f"MC/DC and OpenMC relative difference, t = {time[0]:.3g}")

    def update(frame):
        marker.set_data([time[frame]], [metric[frame]])
        for image, difference in images:
            image.set_data(difference[frame].T)
        title.set_text(f"MC/DC and OpenMC relative difference, t = {time[frame]:.3g}")
        return [title, marker, *(image for image, _ in images)]

    simulation = animation.FuncAnimation(fig, update, frames=len(time))
    simulation.save(
        filename,
        writer=animation.PillowWriter(fps=max(2, len(time) // 10)),
        dpi=120,
    )
    plt.close(fig)


def plot_convergence(score, N_history, difference_l2, difference_max):
    """Plot code-to-code differences with Monte Carlo convergence guides."""
    N_history = np.asarray(N_history)
    difference_l2 = np.asarray(difference_l2)
    difference_max = np.asarray(difference_max)

    fig, ax = plt.subplots()
    ax.plot(
        N_history,
        difference_l2,
        "bo",
        fillstyle="none",
        label="2-norm",
    )
    ax.plot(
        N_history,
        difference_max,
        "gD",
        fillstyle="none",
        label="Maximum",
    )

    for index, difference in enumerate((difference_l2, difference_max)):
        positive = difference > 0.0
        if not np.any(positive):
            continue

        positive_indices = np.flatnonzero(positive)
        anchor = positive_indices[len(positive_indices) // 2]
        expected = 1.0 / np.sqrt(N_history)
        expected *= difference[anchor] / expected[anchor]
        label = r"$O(N^{-1/2})$" if index == 0 else None
        ax.plot(N_history, expected, "r--", label=label)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"Number of particle histories, $N$")
    ax.set_ylabel("Relative difference")
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
