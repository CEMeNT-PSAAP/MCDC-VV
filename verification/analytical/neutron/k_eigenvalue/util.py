import matplotlib.pyplot as plt
import numpy as np


def relative_error(value, reference):
    """Return the relative Euclidean error against a reference array."""
    return np.linalg.norm(value - reference) / np.linalg.norm(reference)


def plot_convergence(name, active_cycles, error):
    """Plot observed error with an active-cycle inverse-square-root guide."""
    midpoint = len(active_cycles) // 2

    plt.plot(active_cycles, error, "bo", fillstyle="none", label="MC/DC")

    expected = 1.0 / np.sqrt(active_cycles)
    expected *= error[midpoint] / expected[midpoint]
    plt.plot(
        active_cycles,
        expected,
        "r--",
        label=r"$O(N_\mathrm{active}^{-0.5})$",
    )

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"Active cycles, $N_\mathrm{active}$")
    plt.ylabel("Relative error")
    plt.title(name)
    plt.grid()
    plt.legend()
    plt.savefig(f"{name}.png")
    plt.clf()
