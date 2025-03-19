import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# S(a,b): c_Graphite (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.0002735],
	['Pu240',1.549e-05],
	['Pu242',5.8e-08],
	['H1',0.0001077],
	['B10',0.00010151],
	['B11',0.00040859],
	['C0',0.0709],
	['O16',0.002705974047],
	['O17',1.025953e-06],
	['Ca40',0.00080267148],
	['Ca42',5.357160000000001e-06],
	['Ca43',1.1178e-06],
	['Ca44',1.727208e-05],
	['Ca46',3.312e-08],
	['Ca48',1.5483599999999998e-06]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=100.0, bc='reflective')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
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

