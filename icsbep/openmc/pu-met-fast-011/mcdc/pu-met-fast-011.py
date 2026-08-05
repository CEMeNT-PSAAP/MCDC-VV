import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.046982],
	['Pu240',0.0025852],
	['Pu242',9.9432e-06]])
# S(a,b): c_H_in_H2O (Not Implemented)
m2 = mcdc.material(nuclides=[
	['H1',0.066766],
	['O16',0.033370347843000005],
	['O17',1.2652157000000001e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.1217, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=29.5217, bc='vacuum')

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

