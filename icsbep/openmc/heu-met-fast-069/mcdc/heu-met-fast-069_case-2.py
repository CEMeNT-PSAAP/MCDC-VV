import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.044736],
	['U238',0.0026745]])
# Material Name: Beryllium
# S(a,b): c_Be (Not Implemented)
m2 = mcdc.material(nuclides=[
	['Be9',0.12056]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=-10.4775, bc='vacuum')
s2 = mcdc.surface('plane-z', z=0.0, bc='interface')
s3 = mcdc.surface('plane-z', z=14.12875, bc='vacuum')
s4 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=8.89, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s2 & -s4, fill=m1)
c2 = mcdc.cell(+s2 & -s3 & -s4, fill=m2)
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

