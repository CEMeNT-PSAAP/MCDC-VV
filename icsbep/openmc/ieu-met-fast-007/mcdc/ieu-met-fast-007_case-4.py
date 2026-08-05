import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

m1 = mcdc.material(nuclides=[
	['U235',0.0049831],
	['U238',0.043108]])
m2 = mcdc.material(nuclides=[
	['U235',0.0048461],
	['U238',0.042695]])
m3 = mcdc.material(nuclides=[
	['U235',0.00034701],
	['U238',0.047846]])
m4 = mcdc.material(nuclides=[
	['U235',0.00010058],
	['U238',0.047677]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.25014, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.10996, bc='interface')
s3 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=7.62, bc='interface')
s4 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=12.54604, bc='interface')
s5 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=26.67, bc='interface')
s6 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=41.91, bc='vacuum')
s7 = mcdc.surface('plane-z', z=-57.4675, bc='vacuum')
s8 = mcdc.surface('plane-z', z=-41.73361, bc='interface')
s9 = mcdc.surface('plane-z', z=-38.24644, bc='interface')
s10 = mcdc.surface('plane-z', z=-22.3901, bc='interface')
s11 = mcdc.surface('plane-z', z=4.35102, bc='interface')
s12 = mcdc.surface('plane-z', z=17.16665, bc='interface')
s13 = mcdc.surface('plane-z', z=23.8125, bc='interface')
s14 = mcdc.surface('plane-z', z=39.0525, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s3 & +s8 & -s10, fill=m2)
c2 = mcdc.cell(-s4 & +s10 & -s11, fill=m2)
c3 = mcdc.cell(-s2 & +s11 & -s13, fill=m2)
c4 = mcdc.cell(-s1 & +s13 & -s14, fill=m2)
c5 = mcdc.cell(+s3 & -s5 & +s8 & -s9, fill=m3)
c6 = mcdc.cell(+s3 & -s5 & +s9 & -s10, fill=m1)
c7 = mcdc.cell(+s4 & -s5 & +s10 & -s11, fill=m1)
c8 = mcdc.cell(+s2 & -s5 & +s11 & -s12, fill=m1)
c9 = mcdc.cell(+s2 & -s5 & +s12 & -s13, fill=m3)
c10 = mcdc.cell(+s5 & -s6 & +s7 & -s14, fill=m4)
c11 = mcdc.cell(-s5 & +s7 & -s8, fill=m4)
c12 = mcdc.cell(+s1 & -s5 & +s13 & -s14, fill=m4)
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

