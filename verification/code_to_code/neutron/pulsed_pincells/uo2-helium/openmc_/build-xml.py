import openmc
import numpy as np

# Materials
fuel = openmc.Material()
fuel.add_nuclide("U235", 0.0001654509603995036)
fuel.add_nuclide("U238", 0.022801089905717036)
fuel.add_nuclide("O16", 0.04593308173223308)
#
moderator = openmc.Material()
moderator.add_nuclide("He4", 0.00024042816805671608)
#
materials = openmc.Materials([fuel, moderator])
materials.export_to_xml()

# Geometry
cylinder = openmc.ZCylinder(r=0.45720, name="Fuel OR")
pitch = 1.25984
box = openmc.model.RectangularPrism(pitch, pitch, boundary_type="reflective")
#
fuel_cell = openmc.Cell(fill=fuel, region=-cylinder)
moderator_cell = openmc.Cell(fill=moderator, region=+cylinder & -box)
#
geometry = openmc.Geometry([fuel_cell, moderator_cell])
geometry.export_to_xml()

# Setting
settings = openmc.Settings()
settings.run_mode = "fixed source"
settings.batches = 30
settings.particles = 10000
settings.cutoff = {"time_neutron": 1.0}
space = openmc.stats.Point()  # At the origin (0, 0, 0)
energy = openmc.stats.delta_function(14.1e6)  # At 14.1 MeV
settings.source = openmc.IndependentSource(space=space, energy=energy)
settings.export_to_xml()

t_grid = np.insert(np.logspace(-9, -4, 200), 0, 0.0)
time_filter = openmc.TimeFilter(t_grid)

e_min, e_max = 1e-5, 20.0e6
groups = 500
energies = np.logspace(np.log10(e_min), np.log10(e_max), groups + 1)
energy_filter = openmc.EnergyFilter(energies)

tally = openmc.Tally()
tally.filters = [time_filter, energy_filter]
tally.scores = ["flux"]

tallies = openmc.Tallies([tally])
tallies.export_to_xml()
