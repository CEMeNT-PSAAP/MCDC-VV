import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Uranyl Nitrate Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.00034118],
	['U238',1.9423e-05],
	['O16',0.035019722493],
	['O17',1.3277507000000002e-05],
	['N14',0.00090231],
	['H1',0.063359]])
# Material Name: Aluminum Tank
m2 = mcdc.material(nuclides=[
	['Al27',0.059469]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=14.005, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=14.325, bc='vacuum')
s3 = mcdc.surface('plane-z', z=-0.64, bc='vacuum')
s4 = mcdc.surface('plane-z', z=0.0, bc='interface')
s5 = mcdc.surface('plane-z', z=33.55, bc='interface')
s6 = mcdc.surface('plane-z', z=41.9, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s2 & +s3 & -s4, fill=m2)
c2 = mcdc.cell(+s1 & -s2 & +s4 & -s6, fill=m2)
c3 = mcdc.cell(-s1 & +s4 & -s5, fill=m1)
c4 = mcdc.cell(-s1 & +s5 & -s6, fill=mvoid)
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

