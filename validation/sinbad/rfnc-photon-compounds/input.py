"""Neutron precursor for the RFNC photon-leakage compound experiment."""

import numpy as np

import mcdc

AVOGADRO_BARN_CM = 0.602214076
SAMPLE = "sio2-sphere"
SAMPLES = {
    "h2o-sphere": (1.0, {"H": 2, "O": 1}),
    "sio2-sphere": (2.2, {"Si": 1, "O": 2}),
    "nacl-sphere": (2.165, {"Na": 1, "Cl": 1}),
}
ATOMIC_WEIGHTS = {
    "H": 1.008,
    "O": 15.999,
    "Si": 28.085,
    "Na": 22.9898,
    "Cl": 35.45,
}


def compound_composition(mass_density, stoichiometry):
    """Return elemental atomic densities for a stoichiometric compound."""
    molecular_weight = sum(
        ATOMIC_WEIGHTS[element] * count for element, count in stoichiometry.items()
    )
    molecule_density = AVOGADRO_BARN_CM * mass_density / molecular_weight
    return {
        element: count * molecule_density for element, count in stoichiometry.items()
    }


if SAMPLE not in SAMPLES:
    raise ValueError(f"Unknown RFNC sample: {SAMPLE}")

simulation = mcdc.Simulation("SINBAD RFNC photon-compound neutron precursor")

# Use provisional bulk densities because the public abstract does not expose the
# sample-parameter table cataloged with the full benchmark.
sample_density, sample_stoichiometry = SAMPLES[SAMPLE]
sample_material = mcdc.Material(
    name=SAMPLE,
    element_composition=compound_composition(
        sample_density,
        sample_stoichiometry,
    ),
)

# Represent the selected full-sphere configuration as a 5-cm-radius source void
# surrounded by a 5-cm-thick compound shell.
inner_surface = mcdc.Surface.Sphere(name="Sample inner surface", radius=5.0)
outer_surface = mcdc.Surface.Sphere(
    name="Sample outer surface",
    radius=10.0,
    boundary_condition="vacuum",
)
source_void = mcdc.Cell(name="Central target void", region=-inner_surface)
sample_shell = mcdc.Cell(
    name="Compound sample",
    region=+inner_surface & -outer_surface,
    fill=sample_material,
)
simulation.set_model([source_void, sample_shell])

# Follow the simplifying source treatment used by the calculation described in
# the public entry.
source = mcdc.Source(
    name="Central isotropic D-T source",
    position=[0.0, 0.0, 0.0],
    isotropic=True,
    energy=14.0e6,
)
simulation.set_sources([source])

# Record neutron leakage as a transport diagnostic until coupled photon
# production and transport can represent the experimental observable.
energy = np.geomspace(1.0e3, 20.0e6, 161)
neutron_leakage = mcdc.Tally(
    name="neutron_leakage_diagnostic",
    surface=outer_surface,
    particle_type="neutron",
    energy=energy,
    scores=["current-out"],
)
simulation.set_tallies([neutron_leakage])

simulation.settings.N_particle = 100_000
simulation.settings.N_batch = 20
simulation.settings.output_name = "output"

simulation.run()
