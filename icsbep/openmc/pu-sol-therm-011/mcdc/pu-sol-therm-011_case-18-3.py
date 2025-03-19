import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium nitrate solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',5.574800000000001e-05],
	['Pu240',2.4339e-06],
	['N14',0.0010468],
	['H1',0.064569],
	['O16',0.035018],
	['Fe54',8.508566500000001e-08],
	['Fe56',1.3356629780000001e-06],
	['Fe57',3.0846283000000005e-08],
	['Fe58',4.105074000000001e-09]])
# Material Name: 347 Stainless Steel
m2 = mcdc.material(nuclides=[
	['Fe54',0.0035295617000000003],
	['Fe56',0.055406570440000004],
	['Fe57',0.00127957934],
	['Fe58',0.00017028851999999998],
	['Cr50',0.0007246590999999999],
	['Cr52',0.013974329419999999],
	['Cr53',0.0015845767799999998],
	['Cr54',0.00039443469999999995],
	['Ni58',0.0067058469576],
	['Ni60',0.0025830802424],
	['Ni61',0.0001122847096],
	['Ni62',0.000358012788],
	['Ni64',9.117530240000001e-05]])
# Material Name: Cadmium
m3 = mcdc.material(nuclides=[
	['Cd106',0.000576933],
	['Cd108',0.0004114992],
	['Cd110',0.005778598],
	['Cd111',0.005929203],
	['Cd112',0.0111721106],
	['Cd113',0.0056659918],
	['Cd114',0.0133246036],
	['Cd116',0.0034810608]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=22.6974, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=22.8244, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=22.8752, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
c3 = mcdc.cell(+s2 & -s3, fill=m3)
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

