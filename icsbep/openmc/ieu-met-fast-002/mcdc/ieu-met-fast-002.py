import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

m1 = mcdc.material(nuclides=[
	['U235',0.007777699999999999],
	['U238',0.039671]])
m2 = mcdc.material(nuclides=[
	['U235',0.00034603],
	['U238',0.047711]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=0.0, bc='vacuum')
s2 = mcdc.surface('plane-z', z=7.62, bc='interface')
s3 = mcdc.surface('plane-z', z=39.571, bc='interface')
s4 = mcdc.surface('plane-z', z=47.0894, bc='vacuum')
s5 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=19.05, bc='interface')
s6 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=26.6446, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s2 & -s6, fill=m2)
c2 = mcdc.cell(+s2 & -s3 & -s5, fill=m1)
c3 = mcdc.cell(+s2 & -s3 & +s5 & -s6, fill=m2)
c4 = mcdc.cell(+s3 & -s4 & -s6, fill=m2)
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
mcdc.source(x=[-10.0,10.0], y=[-10.0,10.0], z=[0.0,47.0894], prob=1.0)

mcdc.run()

