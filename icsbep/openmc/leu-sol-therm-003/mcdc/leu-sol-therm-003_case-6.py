import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Uranyl Nitrate Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',5.0849e-05],
	['U238',0.00044771],
	['N14',0.001534],
	['O16',0.036161289675],
	['O17',1.3710325e-05],
	['H1',0.061685000000000004]])
# Material Name: Stainless steel
m2 = mcdc.material(nuclides=[
	['Fe54',0.0034536936],
	['Fe56',0.05421560352],
	['Fe57',0.00125207472],
	['Fe58',0.00016662816],
	['Cr50',0.0007183154000000001],
	['Cr52',0.013851997480000001],
	['Cr53',0.0015707053200000002],
	['Cr54',0.00039098180000000005],
	['Ni58',0.055393492760999995],
	['Ni60',0.021337474239],
	['Ni61',0.000927525231],
	['Ni62',0.002957356305],
	['Ni64',0.000753151464],
	['Mn55',0.013039],
	['Si28',0.0125460033704],
	['Si29',0.0006370502548],
	['Si30',0.0004199463748],
	['Ti46',0.0049371300000000005],
	['Ti47',0.0044523936],
	['Ti48',0.0441169968],
	['Ti49',0.0032375604],
	['Ti50',0.0030999192]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=43.6303, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=43.8203, bc='vacuum')

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
# Space Type: point
mcdc.source(point=[0.0,0.0,0.0], prob=1.0)

mcdc.run()

