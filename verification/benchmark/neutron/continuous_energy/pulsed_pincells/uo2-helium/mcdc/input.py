import mcdc
import numpy as np

simulation = mcdc.Simulation("Pulsed UO2-helium pincell")

# Material
fuel = mcdc.Material(
    nuclide_composition={
        "U235": 0.0001654509603995036,
        "U238": 0.022801089905717036,
        "O16": 0.04593308173223308,
    }
)
moderator = mcdc.Material(nuclide_composition={"He4": 0.00024042816805671608})

# Geometry
cylinder = mcdc.Surface.CylinderZ(radius=0.45720)
pitch = 1.25984
x0 = mcdc.Surface.PlaneX(x=-pitch / 2, boundary_condition="reflective")
x1 = mcdc.Surface.PlaneX(x=pitch / 2, boundary_condition="reflective")
y0 = mcdc.Surface.PlaneY(y=-pitch / 2, boundary_condition="reflective")
y1 = mcdc.Surface.PlaneY(y=pitch / 2, boundary_condition="reflective")
#
fuel_cell = mcdc.Cell(-cylinder, fill=fuel)
moderator_cell = mcdc.Cell(+x0 & -x1 & +y0 & -y1 & +cylinder, fill=moderator)
simulation.set_model([fuel_cell, moderator_cell])

# Source
source = mcdc.Source(position=[0.0, 0.0, 0.0], isotropic=True, time=0.0, energy=14.1e6)
simulation.set_sources([source])

# Setting
simulation.settings.N_particle = 10000
simulation.settings.N_batch = 30
simulation.settings.time_boundary = 1.0
simulation.settings.active_bank_buffer = 1000

# Tally
t_grid = np.insert(np.logspace(-9, -4, 200), 0, 0.0)
e_min, e_max = 1e-5, 20.0e6
groups = 500
energies = np.logspace(np.log10(e_min), np.log10(e_max), groups + 1)

tally = mcdc.Tally(scores=["flux"], time=t_grid, energy=energies)
simulation.set_tallies([tally])

simulation.run()
