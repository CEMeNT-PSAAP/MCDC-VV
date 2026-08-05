import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: 98% Pu-239 in delta phase
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.036603],
	['Pu240',0.0006691299999999999],
	['Ga69',0.0013197312479999999],
	['Ga71',0.0008758687520000001],
	['Fe54',8.233267000000001e-06],
	['Fe56',0.0001292446844],
	['Fe57',2.9848234e-06],
	['Fe58',3.9722519999999997e-07],
	['C0',0.00028927],
	['Ni58',0.0013264103195999998],
	['Ni60',0.0005109308804],
	['Ni61',2.2209811600000002e-05],
	['Ni62',7.081459800000001e-05],
	['Ni64',1.80343904e-05]])
# Material Name: c_Graphite
# S(a,b): c_Graphite (Not Implemented)
m2 = mcdc.material(nuclides=[
	['C0',0.091842]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.715, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='vacuum')

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

