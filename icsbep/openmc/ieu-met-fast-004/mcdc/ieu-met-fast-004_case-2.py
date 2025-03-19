import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: 36 wt% U-235
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.017384],
	['U238',0.029662],
	['C0',0.00065752],
	['Fe54',7.071281e-06],
	['Fe56',0.0001110039892],
	['Fe57',2.5635662e-06],
	['Fe58',3.411636e-07],
	['W180',1.2145200000000001e-08],
	['W182',2.6820650000000002e-06],
	['W183',1.4483151000000001e-06],
	['W184',3.1010744e-06],
	['W186',2.8774003e-06]])
# Material Name: c_Graphite
# S(a,b): c_Graphite (Not Implemented)
m2 = mcdc.material(nuclides=[
	['C0',0.077716]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=2.788, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=14.0, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=17.2, bc='vacuum')

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

