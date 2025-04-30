import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.042064],
	['U238',0.0043626],
	['C0',0.0011074],
	['Fe54',1.129254e-05],
	['Fe56',0.000177268728],
	['Fe57',4.093908e-06],
	['Fe58',5.44824e-07],
	['W180',6.455759999999999e-08],
	['W182',1.4256470000000001e-05],
	['W183',7.698493800000001e-06],
	['W184',1.6483707200000002e-05],
	['W186',1.5294771400000002e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.0, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.154, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
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

