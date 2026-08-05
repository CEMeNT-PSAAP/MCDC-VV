import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Oralloy
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.047033],
	['U238',0.00047782]])
# Material Name: Lucite
# S(a,b): c_H_in_H2O (Not Implemented)
m2 = mcdc.material(nuclides=[
	['H1',0.05774499999999999],
	['C0',0.03609],
	['O16',0.014435000000000002]])
# Material Name: Water
# S(a,b): c_H_in_H2O (Not Implemented)
m3 = mcdc.material(nuclides=[
	['H1',0.066807],
	['O16',0.033403]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.5537, bc='interface')
s2 = mcdc.surface('plane-z', z=-32.5, bc='vacuum')
s3 = mcdc.surface('plane-z', z=-7.752, bc='interface')
s4 = mcdc.surface('plane-z', z=-5.212, bc='interface')
s5 = mcdc.surface('plane-z', z=23.054, bc='vacuum')
s6 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.974, bc='interface')
s7 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=12.7, bc='interface')
s8 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=30.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s2 & -s3 & +s1 & -s8, fill=m3)
c3 = mcdc.cell(+s3 & -s4 & +s1 & -s6, fill=m3)
c4 = mcdc.cell(+s3 & -s4 & +s6 & -s7, fill=m2)
c5 = mcdc.cell(+s3 & -s4 & +s7 & -s8, fill=m3)
c6 = mcdc.cell(+s4 & -s5 & +s1 & -s8, fill=m3)
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

