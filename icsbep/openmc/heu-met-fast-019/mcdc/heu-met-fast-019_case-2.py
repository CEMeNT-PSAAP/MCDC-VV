import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.042256],
	['U238',0.0043799],
	['C0',0.0010894],
	['Fe54',1.11762245e-05],
	['Fe56',0.0001754428234],
	['Fe57',4.0517399e-06],
	['Fe58',5.392122000000001e-07],
	['W180',6.36228e-08],
	['W182',1.4050035000000002e-05],
	['W183',7.587018900000002e-06],
	['W184',1.62450216e-05],
	['W186',1.5073301700000003e-05]])
# Material Name: c_Graphite
# S(a,b): c_Graphite (Not Implemented)
m2 = mcdc.material(nuclides=[
	['C0',0.076716]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.029, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=12.6, bc='vacuum')

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
# Space Type: point
mcdc.source(point=[0.0,0.0,0.0], prob=1.0)

mcdc.run()

