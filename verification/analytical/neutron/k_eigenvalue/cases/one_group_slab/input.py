"""Define the one-group finite-slab eigenvalue benchmark."""

import numpy as np

import mcdc

LENGTH = 10.0
N_PARTICLE = 10000
N_INACTIVE = 10
N_ACTIVE = 20

simulation = mcdc.Simulation("One-group finite-slab eigenvalue")

# ======================================================================================
# Set model
# ======================================================================================
# Vacuum boundaries produce a leakage-dependent finite-slab eigenfunction.
# The prompt yield is selected to give k = 1.2 for this geometry.

material = mcdc.Material.multigroup(
    capture=np.array([0.25]),
    scatter=np.array([[0.50]]),
    fission=np.array([0.25]),
    nu_p=np.array([2.519421]),
)

lower = mcdc.Surface.PlaneZ(z=0.0, boundary_condition="vacuum")
upper = mcdc.Surface.PlaneZ(z=LENGTH, boundary_condition="vacuum")
cell = mcdc.Cell(region=+lower & -upper, fill=material)
simulation.set_model([cell])

# ======================================================================================
# Set initial source
# ======================================================================================
# A uniform isotropic source initializes iteration toward the finite-slab mode.

source = mcdc.Source(z=[0.0, LENGTH], isotropic=True, energy=0)
simulation.set_sources([source])

# ======================================================================================
# Set tallies, settings, techniques, and run MC/DC
# ======================================================================================

mesh = mcdc.MeshStructured(z=np.linspace(0.0, LENGTH, 101))
tally = mcdc.Tally(mesh=mesh, scores=["flux"])
simulation.set_tallies([tally])

# Particle and inactive-cycle counts stay fixed while the study overrides N_active.
simulation.settings.N_particle = N_PARTICLE
simulation.settings.set_eigenmode(N_inactive=N_INACTIVE, N_active=N_ACTIVE)
simulation.settings.census_bank_buffer_ratio = 2.0
simulation.settings.source_bank_buffer_ratio = 2.0

simulation.technique.population_control()

simulation.run()
