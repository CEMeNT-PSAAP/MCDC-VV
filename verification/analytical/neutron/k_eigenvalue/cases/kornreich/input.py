"""Define the Kornreich-Parsons seven-region slab benchmark."""

import numpy as np

import mcdc

N_PARTICLE = 10000
N_INACTIVE = 20
N_ACTIVE = 20
N_CELL_PER_REGION = 50

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

simulation = mcdc.Simulation("Kornreich-Parsons seven-region slab")

# ======================================================================================
# Set model
# ======================================================================================
# The published data specify nu-Sigma-f rather than Sigma-f and nu separately.
# Assigning all non-scattering fuel removal to fission preserves Sigma-t, Sigma-s,
# and nu-Sigma-f, which fully determine this one-group transport eigenproblem.

fuel_fission = SIGMA_T_FUEL - SIGMA_S
fuel = mcdc.Material.multigroup(
    capture=np.array([0.0]),
    scatter=np.array([[SIGMA_S]]),
    fission=np.array([fuel_fission]),
    nu_p=np.array([NU_SIGMA_F / fuel_fission]),
)
reflector = mcdc.Material.multigroup(
    capture=np.array([SIGMA_T_REFLECTOR - SIGMA_S]),
    scatter=np.array([[SIGMA_S]]),
)

surfaces = [mcdc.Surface.PlaneX(x=REGION_EDGES[0], boundary_condition="vacuum")]
surfaces.extend(mcdc.Surface.PlaneX(x=edge) for edge in REGION_EDGES[1:-1])
surfaces.append(mcdc.Surface.PlaneX(x=REGION_EDGES[-1], boundary_condition="vacuum"))

materials = [reflector, fuel, reflector, fuel, reflector, fuel, reflector]
cells = [
    mcdc.Cell(region=+surfaces[i] & -surfaces[i + 1], fill=material)
    for i, material in enumerate(materials)
]
simulation.set_model(cells)

# ======================================================================================
# Set initial source
# ======================================================================================
# A uniform isotropic source preserves the symmetry of the fundamental mode.

source = mcdc.Source(x=[REGION_EDGES[0], REGION_EDGES[-1]], isotropic=True, energy=0)
simulation.set_sources([source])

# ======================================================================================
# Set tallies, settings, techniques, and run MC/DC
# ======================================================================================

mesh_edges = np.concatenate(
    [
        np.linspace(left, right, N_CELL_PER_REGION + 1)[:-1]
        for left, right in zip(REGION_EDGES[:-1], REGION_EDGES[1:])
    ]
    + [REGION_EDGES[-1:]]
)
mesh = mcdc.MeshStructured(x=mesh_edges)
tally = mcdc.Tally(mesh=mesh, scores=["flux"])
simulation.set_tallies([tally])

# Particle and inactive-cycle counts stay fixed while the study overrides N_active.
simulation.settings.N_particle = N_PARTICLE
simulation.settings.set_eigenmode(N_inactive=N_INACTIVE, N_active=N_ACTIVE)
simulation.settings.census_bank_buffer_ratio = 2.0
simulation.settings.source_bank_buffer_ratio = 2.0

simulation.technique.population_control()

simulation.run()
