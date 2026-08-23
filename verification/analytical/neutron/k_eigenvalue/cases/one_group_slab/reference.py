"""Semi-analytical eigenpair for the one-group finite-slab benchmark."""

import numpy as np
from scipy.linalg import matmul_toeplitz
from scipy.special import expn

LENGTH = 10.0
CAPTURE = 0.25
SCATTER = 0.50
FISSION = 0.25
NU_PROMPT = 2.519421
REFINEMENT = 40
TOTAL = CAPTURE + SCATTER + FISSION


def _collision_kernel_first_column(N):
    """Return the cell-integrated E1 kernel for a uniform fine mesh."""
    width = LENGTH / N
    column = np.empty(N)

    # Integrate the logarithmic diagonal singularity analytically.
    half_optical_width = 0.5 * TOTAL * width
    column[0] = 2.0 / TOTAL * (1.0 - expn(2, half_optical_width))

    offset = np.arange(1, N)
    lower_distance = TOTAL * (offset - 0.5) * width
    upper_distance = TOTAL * (offset + 0.5) * width
    column[1:] = (expn(2, lower_distance) - expn(2, upper_distance)) / TOTAL
    return column


def _dominant_eigenpair(column):
    """Solve the positive symmetric Toeplitz eigenproblem by power iteration."""
    flux = np.ones(len(column))
    flux /= np.linalg.norm(flux)
    eigenvalue_previous = 0.0

    for _ in range(500):
        product = matmul_toeplitz(
            (column, column),
            flux,
            check_finite=False,
        )
        eigenvalue = float(flux @ product)
        flux = product / np.linalg.norm(product)

        if abs(eigenvalue - eigenvalue_previous) <= 1.0e-13 * eigenvalue:
            break
        eigenvalue_previous = eigenvalue
    else:
        raise RuntimeError("Finite-slab reference power iteration did not converge.")

    return eigenvalue, flux


def reference(z):
    """Return the finite-slab multiplication factor and cell-averaged flux."""
    z = np.asarray(z)
    dz = np.diff(z)

    if not np.allclose(dz, dz[0]):
        raise ValueError("Finite-slab reference requires a uniform tally mesh.")
    if not np.isclose(z[0], 0.0) or not np.isclose(z[-1], LENGTH):
        raise ValueError("Finite-slab reference mesh must span the full slab.")

    N_cell = len(dz)
    N_fine = REFINEMENT * N_cell
    kernel_column = _collision_kernel_first_column(N_fine)
    kernel_eigenvalue, fine_flux = _dominant_eigenpair(kernel_column)

    critical_collision_source = 2.0 / kernel_eigenvalue
    k_effective = NU_PROMPT * FISSION / (critical_collision_source - SCATTER)

    fine_width = LENGTH / N_fine
    fine_flux /= np.sum(fine_flux * fine_width)
    flux = np.mean(fine_flux.reshape(N_cell, REFINEMENT), axis=1)
    return k_effective, flux
