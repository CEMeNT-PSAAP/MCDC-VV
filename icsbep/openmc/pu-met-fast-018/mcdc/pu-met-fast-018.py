import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.037291],
	['Pu240',0.0019277],
	['Ga69',0.0008191518239999999],
	['Ga71',0.0005436481759999999]])
# S(a,b): c_Be (Not Implemented)
m2 = mcdc.material(nuclides=[
	['Be9',0.11984],
	['O16',0.0013770778896],
	['O17',5.221104000000001e-07]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.0419, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.73, bc='vacuum')

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

