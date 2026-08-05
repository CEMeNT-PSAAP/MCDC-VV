import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.042315],
	['U238',0.0043901],
	['C0',0.0010548],
	['Fe54',1.08874815e-05],
	['Fe56',0.0001709101758],
	['Fe57',3.9470613e-06],
	['Fe58',5.252813999999999e-07],
	['W180',6.2448e-08],
	['W182',1.3790600000000001e-05],
	['W183',7.446924000000001e-06],
	['W184',1.5945056e-05],
	['W186',1.4794972000000003e-05]])
# Material Name: Polyethylene
# S(a,b): c_H_in_CH2 (Not Implemented)
m2 = mcdc.material(nuclides=[
	['H1',0.077711],
	['C0',0.038856]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.8, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
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

