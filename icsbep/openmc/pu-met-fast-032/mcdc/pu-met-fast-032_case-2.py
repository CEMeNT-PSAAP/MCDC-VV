import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.042126],
	['Pu240',0.0045761],
	['Fe54',1.67278055e-05],
	['Fe56',0.0002625907726],
	['Fe57',6.064366100000001e-06],
	['Fe58',8.070558000000001e-07],
	['C0',0.00126],
	['H1',0.00032394954024],
	['H2',5.045976e-08],
	['N14',3.4843897564000004e-05],
	['N15',1.28102436e-07],
	['O16',5.1823351502999994e-05],
	['O17',1.9648496999999998e-08]])
# Material Name: Steel reflector
m2 = mcdc.material(nuclides=[
	['Fe54',0.0046715578],
	['Fe56',0.07333346696],
	['Fe57',0.0016935895599999998],
	['Fe58',0.00022538567999999998],
	['C0',0.0011341],
	['Si28',0.000149107723656],
	['Si29',7.5712647719999995e-06],
	['Si30',4.991011571999999e-06],
	['Cr50',1.1383031e-05],
	['Cr52',0.0002195104222],
	['Cr53',2.48907198e-05],
	['Cr54',6.195827e-06],
	['Mn55',0.00033061],
	['Ni58',0.00015800648489999999],
	['Ni60',6.086381509999999e-05],
	['Ni61',2.6457078999999998e-06],
	['Ni62',8.435674500000001e-06],
	['Ni64',2.1483176e-06],
	['Cu63',0.000148236855],
	['Cu65',6.6133145e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.7, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
c3 = mcdc.cell(+s2 & -s3, fill=m2)
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

