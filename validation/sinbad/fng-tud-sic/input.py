"""Public-entry reconstruction of the FNG/TUD SiC spectral experiment."""

import numpy as np

import mcdc

AVOGADRO_BARN_CM = 0.602214076
DETECTOR_POSITIONS = {
    "p1": 12.70,
    "p2": 27.94,
    "p3": 43.18,
    "p4": 58.42,
}
TALLY_HALF_WIDTH = 0.1


def atomic_density(mass_density, mass_fraction, atomic_weight):
    """Convert a mass fraction and density to atoms/(barn cm)."""
    return AVOGADRO_BARN_CM * mass_density * mass_fraction / atomic_weight


simulation = mcdc.Simulation("SINBAD FNG/TUD SiC public-entry model")

# Use the bulk composition stated in the public SINBAD abstract.
sic = mcdc.Material(
    name="FNG SiC block",
    element_composition={
        "Si": atomic_density(3.158, 0.689, 28.085),
        "C": atomic_density(3.158, 0.308, 12.011),
        "B": atomic_density(3.158, 0.0019, 10.81),
        "Al": atomic_density(3.158, 0.00079, 26.9815),
        "Fe": atomic_density(3.158, 0.00014, 55.845),
    },
)

# Approximate the brick assembly by one homogeneous block preceded by a void
# region containing the FNG target position.
x_source = mcdc.Surface.PlaneX(x=-5.31, boundary_condition="vacuum")
x_front = mcdc.Surface.PlaneX(x=0.0)
x_back = mcdc.Surface.PlaneX(x=71.1, boundary_condition="vacuum")
y_min = mcdc.Surface.PlaneY(y=-22.85, boundary_condition="vacuum")
y_max = mcdc.Surface.PlaneY(y=22.85, boundary_condition="vacuum")
z_min = mcdc.Surface.PlaneZ(z=-22.85, boundary_condition="vacuum")
z_max = mcdc.Surface.PlaneZ(z=22.85, boundary_condition="vacuum")
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

# Replace the tabulated angle-energy source by a monoenergetic isotropic source
# at the reported 5.3 cm stand-off.
source = mcdc.Source(
    name="FNG D-T source approximation",
    position=[-5.3, 0.0, 0.0],
    isotropic=True,
    energy=14.0e6,
)
simulation.set_sources([source])

# Sample the neutron spectrum in small volumes centered on the four reported
# detector positions without perturbing the block with provisional detector cells.
energy = np.geomspace(1.0e3, 20.0e6, 161)
tallies = []
for label, x in DETECTOR_POSITIONS.items():
    mesh = mcdc.MeshStructured(
        x=[x - TALLY_HALF_WIDTH, x + TALLY_HALF_WIDTH],
        y=[-TALLY_HALF_WIDTH, TALLY_HALF_WIDTH],
        z=[-TALLY_HALF_WIDTH, TALLY_HALF_WIDTH],
    )
    tallies.append(
        mcdc.Tally(
            name=f"neutron_flux_{label}",
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
