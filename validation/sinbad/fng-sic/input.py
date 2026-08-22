"""Public-entry reconstruction of the integral FNG SiC experiment."""

import numpy as np

import mcdc

AVOGADRO_BARN_CM = 0.602214076
ACTIVATION_POSITIONS = [10.41, 25.65, 40.89, 56.13]
HEATING_POSITIONS = [14.99, 30.23, 45.47, 60.71]
TALLY_HALF_WIDTH = 0.1


def atomic_density(mass_density, mass_fraction, atomic_weight):
    """Convert a mass fraction and density to atoms/(barn cm)."""
    return AVOGADRO_BARN_CM * mass_density * mass_fraction / atomic_weight


simulation = mcdc.Simulation("SINBAD FNG SiC public-entry model")

# Allocate the composition remaining after the listed impurities to
# stoichiometric SiC.
impurities = {"B": 0.0019, "Al": 0.0079, "Fe": 0.0014}
sic_fraction = 1.0 - sum(impurities.values())
silicon_fraction = sic_fraction * 28.085 / (28.085 + 12.011)
carbon_fraction = sic_fraction - silicon_fraction
mass_fractions = {
    "Si": silicon_fraction,
    "C": carbon_fraction,
    **impurities,
}
atomic_weights = {
    "Si": 28.085,
    "C": 12.011,
    "B": 10.81,
    "Al": 26.9815,
    "Fe": 55.845,
}
sic = mcdc.Material(
    name="FNG SiC block",
    element_composition={
        element: atomic_density(3.158, fraction, atomic_weights[element])
        for element, fraction in mass_fractions.items()
    },
)

# Approximate the brick mock-up by a homogeneous block with a source-side void.
x_source = mcdc.Surface.PlaneX(x=-5.31, boundary_condition="vacuum")
x_front = mcdc.Surface.PlaneX(x=0.0)
x_back = mcdc.Surface.PlaneX(x=71.12, boundary_condition="vacuum")
y_min = mcdc.Surface.PlaneY(y=-22.86, boundary_condition="vacuum")
y_max = mcdc.Surface.PlaneY(y=22.86, boundary_condition="vacuum")
z_min = mcdc.Surface.PlaneZ(z=-22.86, boundary_condition="vacuum")
z_max = mcdc.Surface.PlaneZ(z=22.86, boundary_condition="vacuum")
transverse_region = +y_min & -y_max & +z_min & -z_max

source_void = mcdc.Cell(
    name="Source-side void",
    region=+x_source & -x_front & transverse_region,
)
sic_block = mcdc.Cell(
    name="Homogenized SiC block",
    region=+x_front & -x_back & transverse_region,
    fill=sic,
)
simulation.set_model([source_void, sic_block])

# Replace the public entry's tabulated angle-energy distribution by a 14 MeV
# isotropic point source at the reported stand-off.
source = mcdc.Source(
    name="FNG D-T source approximation",
    position=[-5.3, 0.0, 0.0],
    isotropic=True,
    energy=14.0e6,
)
simulation.set_sources([source])

# Record neutron spectra at the foil and TLD depths for later response folding.
energy = np.geomspace(1.0e-3, 20.0e6, 241)
tallies = []
for kind, positions in (
    ("activation", ACTIVATION_POSITIONS),
    ("heating", HEATING_POSITIONS),
):
    for index, x in enumerate(positions, start=1):
        mesh = mcdc.MeshStructured(
            x=[x - TALLY_HALF_WIDTH, x + TALLY_HALF_WIDTH],
            y=[-TALLY_HALF_WIDTH, TALLY_HALF_WIDTH],
            z=[-TALLY_HALF_WIDTH, TALLY_HALF_WIDTH],
        )
        tallies.append(
            mcdc.Tally(
                name=f"{kind}_flux_p{index}",
                mesh=mesh,
                particle_type="neutron",
                energy=energy,
                scores=["flux"],
            )
        )
simulation.set_tallies(tallies)

simulation.settings.N_particle = 100_000
simulation.settings.N_batch = 20
simulation.settings.output_name = "output"

simulation.run()
