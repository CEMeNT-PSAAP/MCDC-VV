"""Semi-analytical eigenpair for the Kornreich-Parsons base case."""

import numpy as np
from scipy.linalg import matmul_toeplitz
from scipy.special import expn

K_EFFECTIVE = 1.17361
REFINEMENT = 8

SIGMA_T_FUEL = 0.415
SIGMA_T_REFLECTOR = 0.371
SIGMA_S = 0.334
NU_SIGMA_F = 0.178

FUEL_WIDTH = 1.0 / SIGMA_T_FUEL
REFLECTOR_WIDTH = 1.0 / SIGMA_T_REFLECTOR
REGION_WIDTHS = np.array(
    [
        REFLECTOR_WIDTH,
        FUEL_WIDTH,
        REFLECTOR_WIDTH,
        FUEL_WIDTH,
        REFLECTOR_WIDTH,
        FUEL_WIDTH,
        REFLECTOR_WIDTH,
    ]
)
REGION_EDGES = np.concatenate(([0.0], np.cumsum(REGION_WIDTHS)))


def _expected_mesh(N_cell_per_region):
    """Return a mesh with equal optical-width cells in every region."""
    return np.concatenate(
        [
            np.linspace(left, right, N_cell_per_region + 1)[:-1]
            for left, right in zip(REGION_EDGES[:-1], REGION_EDGES[1:])
        ]
        + [REGION_EDGES[-1:]]
    )


def _collision_kernel_first_column(N_cell_per_region):
    """Return the cell-integrated E1 kernel on the uniform optical mesh."""
    N = 7 * N_cell_per_region
    optical_width = 1.0 / N_cell_per_region
    column = np.empty(N)

    # Integrate the logarithmic diagonal singularity analytically.
    column[0] = 2.0 * (1.0 - expn(2, 0.5 * optical_width))

    offset = np.arange(1, N)
    lower_distance = (offset - 0.5) * optical_width
    upper_distance = (offset + 0.5) * optical_width
    column[1:] = expn(2, lower_distance) - expn(2, upper_distance)
    return column


def _kernel_product(column, vector):
    """Apply one half of the collision kernel to a source vector."""
    return 0.5 * matmul_toeplitz(
        (column, column),
        vector,
        check_finite=False,
    )


def _fixed_source_solve(column, scatter_ratio, source, initial):
    """Converge the within-generation isotropic scattering source."""
    flux = initial.copy()

    for _ in range(1000):
        updated = source + _kernel_product(column, scatter_ratio * flux)
        if np.linalg.norm(updated - flux) <= 1.0e-13 * np.linalg.norm(updated):
            return updated
        flux = updated

    raise RuntimeError("Kornreich reference scattering iteration did not converge.")


def _dominant_eigenpair(column, scatter_ratio, fission_ratio):
    """Solve the positive transport eigenproblem by power iteration."""
    flux = np.ones(len(column))
    flux /= np.linalg.norm(flux)
    eigenvalue_previous = 0.0

    for _ in range(200):
        fission_source = _kernel_product(column, fission_ratio * flux)
        updated = _fixed_source_solve(
            column,
            scatter_ratio,
            fission_source,
            flux,
        )
        eigenvalue = float(flux @ updated / (flux @ flux))
        updated /= np.linalg.norm(updated)

        if abs(eigenvalue - eigenvalue_previous) <= 1.0e-12 * eigenvalue:
            return eigenvalue, updated
        eigenvalue_previous = eigenvalue
        flux = updated

    raise RuntimeError("Kornreich reference power iteration did not converge.")


def reference(x):
    """Return the published eigenvalue and semi-analytical cell-averaged flux."""
    x = np.asarray(x)
    N_cell = len(x) - 1

    if N_cell % 7 != 0:
        raise ValueError("Kornreich reference requires equal cell counts per region.")

    N_cell_per_region = N_cell // 7
    if not np.allclose(x, _expected_mesh(N_cell_per_region)):
        raise ValueError("Kornreich reference mesh must use equal optical-width cells.")

    N_fine_per_region = REFINEMENT * N_cell_per_region
    is_fuel = np.tile(
        np.concatenate(
            (
                np.zeros(N_fine_per_region, dtype=bool),
                np.ones(N_fine_per_region, dtype=bool),
            )
        ),
        3,
    )
    is_fuel = np.concatenate((is_fuel, np.zeros(N_fine_per_region, dtype=bool)))

    total = np.where(is_fuel, SIGMA_T_FUEL, SIGMA_T_REFLECTOR)
    scatter_ratio = SIGMA_S / total
    fission_ratio = np.where(is_fuel, NU_SIGMA_F / total, 0.0)

    column = _collision_kernel_first_column(N_fine_per_region)
    computed_k, fine_flux = _dominant_eigenpair(
        column,
        scatter_ratio,
        fission_ratio,
    )
    if not np.isclose(computed_k, K_EFFECTIVE, rtol=1.0e-6):
        raise RuntimeError(
            "Kornreich integral reference does not reproduce published k-effective."
        )

    optical_width = 1.0 / N_fine_per_region
    fine_dx = optical_width / total
    fine_flux /= np.sum(fine_flux * fine_dx)
    flux = np.mean(
        fine_flux.reshape(N_cell, REFINEMENT),
        axis=1,
    )
    return K_EFFECTIVE, flux
