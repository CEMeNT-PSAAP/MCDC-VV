"""Public-entry reconstruction of the OKTAVIAN 60-cm silicon sphere."""

import numpy as np

import mcdc

AVOGADRO_BARN_CM = 0.602214076


def atomic_density(mass_density, mass_fraction, atomic_weight):
    """Convert a mass fraction and density to atoms/(barn cm)."""
    return AVOGADRO_BARN_CM * mass_density * mass_fraction / atomic_weight


simulation = mcdc.Simulation("SINBAD OKTAVIAN Si-60 public-entry model")

# Build the natural-element materials from the densities and compositions stated in
# the public SINBAD entry.
silicon = mcdc.Material(
    name="Granular natural silicon",
    element_composition={
        "Si": atomic_density(1.29, 1.0, 28.085),
    },
)
stainless_steel = mcdc.Material(
    name="JIS SUS-304 approximation",
    element_composition={
        "Cr": atomic_density(7.86, 0.185, 51.9961),
        "Fe": atomic_density(7.86, 0.704, 55.845),
        "Ni": atomic_density(7.86, 0.111, 58.6934),
    },
)

# Represent the Type-III vessel as concentric spheres with a one-sided, void
# reentrant hole along +z.
inner_void = mcdc.Surface.Sphere(name="Inner void", radius=10.0)
inner_vessel = mcdc.Surface.Sphere(name="Inner vessel outer wall", radius=10.2)
silicon_outer = mcdc.Surface.Sphere(name="Silicon outer surface", radius=30.0)
vessel_outer = mcdc.Surface.Sphere(
    name="Vessel outer surface",
    radius=30.5,
    boundary_condition="vacuum",
)
beam_duct = mcdc.Surface.CylinderZ(name="Reentrant hole", radius=5.5)
duct_midplane = mcdc.Surface.PlaneZ(name="Reentrant-hole midplane", z=0.0)

reentrant_hole = -beam_duct & +duct_midplane & -vessel_outer
source_void_cell = mcdc.Cell(name="Central source void", region=-inner_void)
duct_void_cell = mcdc.Cell(
    name="Reentrant-hole void",
    region=reentrant_hole & +inner_void,
)
inner_vessel_cell = mcdc.Cell(
    name="Inner stainless-steel vessel",
    region=+inner_void & -inner_vessel & ~reentrant_hole,
    fill=stainless_steel,
)
silicon_cell = mcdc.Cell(
    name="Granular silicon pile",
    region=+inner_vessel & -silicon_outer & ~reentrant_hole,
    fill=silicon,
)
outer_vessel_cell = mcdc.Cell(
    name="Outer stainless-steel vessel",
    region=+silicon_outer & -vessel_outer & ~reentrant_hole,
    fill=stainless_steel,
)
simulation.set_model(
    [
        source_void_cell,
        duct_void_cell,
        inner_vessel_cell,
        silicon_cell,
        outer_vessel_cell,
    ]
)

# The public entry states that benchmark analyses assume isotropic emission but does
# not expose its tabulated source spectrum, so this preliminary model uses 14 MeV.
source = mcdc.Source(
    name="Central isotropic D-T source",
    position=[0.0, 0.0, 0.0],
    isotropic=True,
    energy=14.0e6,
)
simulation.set_sources([source])

# Score the outward leakage current per source neutron on the vessel surface.
energy = np.geomspace(1.0e4, 20.0e6, 161)
leakage = mcdc.Tally(
    name="neutron_leakage",
    surface=vessel_outer,
    particle_type="neutron",
    energy=energy,
    scores=["current-out"],
)
simulation.set_tallies([leakage])

# Provide a useful exploratory run while leaving production histories to the suite
# launcher once this case is integrated into the validation workflow.
simulation.settings.N_particle = 100_000
simulation.settings.N_batch = 20
simulation.settings.output_name = "output"

simulation.run()
