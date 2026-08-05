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
s1 = mcdc.surface('plane-x', x=-25.4, bc='vacuum')
s2 = mcdc.surface('plane-x', x=-5.08, bc='interface')
s3 = mcdc.surface('plane-x', x=5.08, bc='interface')
s4 = mcdc.surface('plane-x', x=25.4, bc='vacuum')
s5 = mcdc.surface('plane-y', y=-25.4, bc='vacuum')
s6 = mcdc.surface('plane-y', y=-5.08, bc='interface')
s7 = mcdc.surface('plane-y', y=5.08, bc='interface')
s8 = mcdc.surface('plane-y', y=25.4, bc='vacuum')
s9 = mcdc.surface('plane-z', z=-24.97, bc='vacuum')
s10 = mcdc.surface('plane-z', z=-4.65, bc='interface')
s11 = mcdc.surface('plane-z', z=4.65, bc='interface')
s12 = mcdc.surface('plane-z', z=24.97, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s2 & +s5 & -s8 & +s9 & -s12, fill=m2)
c2 = mcdc.cell(+s2 & -s3 & +s5 & -s6 & +s9 & -s12, fill=m2)
c3 = mcdc.cell(+s2 & -s3 & +s6 & -s7 & +s9 & -s10, fill=m2)
c4 = mcdc.cell(+s2 & -s3 & +s6 & -s7 & +s10 & -s11, fill=m1)
c5 = mcdc.cell(+s2 & -s3 & +s6 & -s7 & +s11 & -s12, fill=m2)
c6 = mcdc.cell(+s2 & -s3 & +s7 & -s8 & +s9 & -s12, fill=m2)
c7 = mcdc.cell(+s3 & -s4 & +s5 & -s8 & +s9 & -s12, fill=m2)
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

