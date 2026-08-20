"""Analytical manufactured fields for the fixed-source two-group slab case."""

import numpy as np
from scipy.special import expn

LENGTH = 10.0
TOTAL_SOURCE_STRENGTH = 14.3

# R_g(x) = intercept_g + slope_g * x is the manufactured total isotropic
# right-hand side of the transport equation.
INTERCEPT = np.array([0.5, 0.6])
SLOPE = np.array([0.01, -0.01])
SCATTER_SOURCE = 0.22


def total_rhs(x):
    """Return the manufactured isotropic transport right-hand side."""
    x = np.atleast_1d(x)
    return INTERCEPT[:, None] + SLOPE[:, None] * x


def scalar_source(x):
    """Return the angle-integrated external volumetric source."""
    return 2.0 * (total_rhs(x) - SCATTER_SOURCE)


def angular_flux(x, mu):
    """Return the exact angular flux per total external source particle."""
    x = np.atleast_1d(x)
    mu = np.atleast_1d(mu)
    x_grid, mu_grid = np.meshgrid(x, mu, indexing="ij")
    distance = np.where(mu_grid > 0.0, x_grid, LENGTH - x_grid)

    flux = np.empty((2, len(x), len(mu)))
    for group in range(2):
        rhs = INTERCEPT[group] + SLOPE[group] * x_grid
        correction = np.zeros_like(x_grid)
        nonzero = mu_grid != 0.0
        correction[nonzero] = (
            mu_grid[nonzero]
            * SLOPE[group]
            * np.exp(-distance[nonzero] / np.abs(mu_grid[nonzero]))
        )
        flux[group] = rhs - mu_grid * SLOPE[group] + correction

    return flux / TOTAL_SOURCE_STRENGTH


def scalar_flux(x):
    """Return the exact scalar flux per total external source particle."""
    x = np.atleast_1d(x)
    boundary_term = expn(3, x) - expn(3, LENGTH - x)

    flux = np.empty((2, len(x)))
    for group in range(2):
        rhs = INTERCEPT[group] + SLOPE[group] * x
        flux[group] = 2.0 * rhs + SLOPE[group] * boundary_term

    return flux / TOTAL_SOURCE_STRENGTH


def cell_average_scalar_flux(x):
    """Return exact cell averages per total external source particle."""
    x = np.atleast_1d(x)
    dx = np.diff(x)

    # -E_4(x) - E_4(L-x) is an antiderivative of
    # E_3(x) - E_3(L-x).
    boundary_antiderivative = -expn(4, x) - expn(4, LENGTH - x)
    boundary_average = np.diff(boundary_antiderivative) / dx
    x_average = 0.5 * (x[:-1] + x[1:])

    flux = np.empty((2, len(dx)))
    for group in range(2):
        rhs_average = INTERCEPT[group] + SLOPE[group] * x_average
        flux[group] = 2.0 * rhs_average + SLOPE[group] * boundary_average

    return flux / TOTAL_SOURCE_STRENGTH
