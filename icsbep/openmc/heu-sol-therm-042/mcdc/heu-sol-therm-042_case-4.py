import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Uranyl Nitrate Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',3.4834e-05],
	['U238',1.9615e-06],
	['N14',0.00012091],
	['H1',0.066319],
	['O16',0.033561275454],
	['O17',1.2724545999999997e-05]])
# Material Name: SS-304 Tank
m2 = mcdc.material(nuclides=[
	['Fe54',0.00340179],
	['Fe56',0.053400828000000004],
	['Fe57',0.001233258],
	['Fe58',0.000164124],
	['C0',0.00031687],
	['Cr50',0.0006758213000000001],
	['Cr52',0.01303254106],
	['Cr53',0.00147778554],
	['Cr54',0.0003678521000000001],
	['Ni58',0.0066220442937],
	['Ni60',0.0025507996062999997],
	['Ni61',0.00011088149269999999],
	['Ni62',0.00035353871850000003],
	['Ni64',9.00358888e-05],
	['Mo100',0.00012079636800000002],
	['Mo92',0.00018160365299999998],
	['Mo94',0.00011389123899999999],
	['Mo95',0.000196777581],
	['Mo96',0.000206695181],
	['Mo97',0.000118788054],
	['Mo98',0.00030114792400000003],
	['N14',0.00033841582542],
	['N15',1.24417458e-06]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=77.3684, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=77.6986, bc='vacuum')
s3 = mcdc.surface('plane-z', z=-0.3302, bc='vacuum')
s4 = mcdc.surface('plane-z', z=0.0, bc='interface')
s5 = mcdc.surface('plane-z', z=105.283, bc='interface')
s6 = mcdc.surface('plane-z', z=304.8, bc='vacuum')

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

