"""Define the analytical two-group slab MMS fixed-source problem."""

import numpy as np

import mcdc

LENGTH = 10.0

simulation = mcdc.Simulation("Two-group slab manufactured solution")

# ======================================================================================
# Set model
# ======================================================================================
# The identical scattering columns make the two groups' opposite boundary-layer
# contributions cancel in the isotropic scattering source.

material = mcdc.Material.multigroup(
    capture=np.array([0.6, 0.6]),
    scatter=np.full((2, 2), 0.2),
)

left = mcdc.Surface.PlaneX(x=0.0, boundary_condition="vacuum")
right = mcdc.Surface.PlaneX(x=LENGTH, boundary_condition="vacuum")
cell = mcdc.Cell(region=+left & -right, fill=material)
simulation.set_model([cell])

# ======================================================================================
# Set sources
# ======================================================================================
# Each positive linear volume-source profile is sampled exactly by the tabulated
# spatial PDF. Raw probabilities are the corresponding integrated source rates.

volume_source_1 = mcdc.Source(
    x=([0.0, LENGTH], [0.56, 0.76]),
    isotropic=True,
    energy=0,
    probability=6.6,
)
volume_source_2 = mcdc.Source(
    x=([0.0, LENGTH], [0.76, 0.56]),
    isotropic=True,
    energy=1,
    probability=6.6,
)

# The manufactured incoming angular flux is isotropic on each boundary, so white
# half-space sources sample its incident-current distribution exactly.
boundary_sources = [
    mcdc.Source(
        position=(0.0, 0.0, 0.0),
        white_direction=(1.0, 0.0, 0.0),
        energy=0,
        probability=0.25,
    ),
    mcdc.Source(
        position=(0.0, 0.0, 0.0),
        white_direction=(1.0, 0.0, 0.0),
        energy=1,
        probability=0.30,
    ),
    mcdc.Source(
        position=(LENGTH, 0.0, 0.0),
        white_direction=(-1.0, 0.0, 0.0),
        energy=0,
        probability=0.30,
    ),
    mcdc.Source(
        position=(LENGTH, 0.0, 0.0),
        white_direction=(-1.0, 0.0, 0.0),
        energy=1,
        probability=0.25,
    ),
]
simulation.set_sources([volume_source_1, volume_source_2, *boundary_sources])

# ======================================================================================
# Set tallies, settings, and run MC/DC
# ======================================================================================

mesh = mcdc.MeshStructured(x=np.linspace(0.0, LENGTH, 101))
tally = mcdc.Tally(mesh=mesh, energy="all", scores=["flux"])
simulation.set_tallies([tally])

simulation.settings.N_particle = 100
simulation.settings.N_batch = 2

simulation.run()
