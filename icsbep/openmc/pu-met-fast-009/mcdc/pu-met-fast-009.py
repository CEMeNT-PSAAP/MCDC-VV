import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Core
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.037592],
	['Pu240',0.0019349],
	['Ga69',0.0008254631639999998],
	['Ga71',0.000547836836]])
# Material Name: Reflector
m2 = mcdc.material(nuclides=[
	['Al27',0.058787],
	['Cu63',0.0008131348499999999],
	['Cu65',0.00036276514999999997],
	['Si28',0.000223075927016],
	['Si29',1.1327159091999999e-05],
	['Si30',7.466913892e-06],
	['Mn55',0.00024729],
	['Mg24',0.0002758232136],
	['Mg25',3.5005872e-05],
	['Mg26',3.85309144e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.5118, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=13.4366, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

##############################
#__________Settings__________
##############################

# Simulation Parameters
mcdc.eigenmode(N_inactive=20, N_active=180)
mcdc.setting(N_particle=10000)

# Source Parameters
# Particle: neutron
# Space Type: box
mcdc.source(x=[-1.0,1.0], y=[-1.0,1.0], z=[-1.0,1.0], prob=1.0)

mcdc.run()

