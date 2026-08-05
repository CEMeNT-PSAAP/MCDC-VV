import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.044605],
	['U238',0.0025315]])
# Material Name: Beryllium
# S(a,b): c_Be (Not Implemented)
m2 = mcdc.material(nuclides=[
	['Be9',0.12295]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.64241, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=17.42801, bc='vacuum')

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
# Space Type: point
mcdc.source(point=[0.0,0.0,0.0], prob=1.0)

mcdc.run()

