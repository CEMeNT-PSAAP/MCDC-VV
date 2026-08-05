import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

m1 = mcdc.material(nuclides=[
	['U235',0.044917],
	['U238',0.0025993]])
m2 = mcdc.material(nuclides=[
	['U235',0.00034428],
	['U238',0.04747]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=5.1706, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=25.4906, bc='vacuum')
s3 = mcdc.surface('plane-z', z=-26.035, bc='vacuum')
s4 = mcdc.surface('plane-z', z=-5.715, bc='interface')
s5 = mcdc.surface('plane-z', z=5.715, bc='interface')
s6 = mcdc.surface('plane-z', z=25.035, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s2 & +s3 & -s4, fill=m2)
c2 = mcdc.cell(-s1 & +s4 & -s5, fill=m1)
c3 = mcdc.cell(+s1 & -s2 & +s4 & -s5, fill=m2)
c4 = mcdc.cell(-s2 & +s5 & -s6, fill=m2)
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

