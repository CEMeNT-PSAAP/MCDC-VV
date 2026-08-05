import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium core
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.036049],
	['Pu240',0.0019562],
	['Ga69',0.000801720504],
	['Ga71',0.000532079496]])
# Material Name: Thorium reflector
# Depletable
m2 = mcdc.material(nuclides=[
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.31, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=26.67, bc='vacuum')
s3 = mcdc.surface('plane-z', z=-26.67, bc='vacuum')
s4 = mcdc.surface('plane-z', z=26.67, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2 & +s3 & -s4, fill=m2)
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

