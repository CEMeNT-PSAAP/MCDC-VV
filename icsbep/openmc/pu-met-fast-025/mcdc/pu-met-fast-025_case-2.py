import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.036704],
	['Pu240',0.00067099],
	['Ga69',0.0013231574039999998],
	['Ga71',0.0008781425959999998],
	['Fe54',8.2759355e-06],
	['Fe56',0.0001299144886],
	['Fe57',3.0002921e-06],
	['Fe58',3.992838000000001e-07],
	['C0',0.00029038],
	['Ni58',0.0013475141586000003],
	['Ni60',0.0005190600414],
	['Ni61',2.25631806e-05],
	['Ni62',7.1941293e-05],
	['Ni64',1.83213264e-05]])
# Material Name: Steel reflector
m2 = mcdc.material(nuclides=[
	['Fe54',0.00465010665],
	['Fe56',0.07299672978],
	['Fe57',0.0016858128300000002],
	['Fe58',0.00022435074],
	['C0',0.0011289],
	['Si28',0.000148425224024],
	['Si29',7.536609388e-06],
	['Si30',4.968166588e-06],
	['Cr50',1.1330891e-05],
	['Cr52',0.0002185049542],
	['Cr53',2.47767078e-05],
	['Cr54',6.167447000000001e-06],
	['Mn55',0.00032909],
	['Ni58',0.00015728486976],
	['Ni60',6.0585850240000005e-05],
	['Ni61',2.6336249599999996e-06],
	['Ni62',8.3971488e-06],
	['Ni64',2.13850624e-06],
	['Cu63',0.00014755227],
	['Cu65',6.582773e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='vacuum')

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

