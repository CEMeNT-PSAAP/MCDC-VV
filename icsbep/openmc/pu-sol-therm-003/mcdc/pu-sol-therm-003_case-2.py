import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium nitrate solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',8.4936e-05],
	['Pu240',1.5153e-06],
	['N14',0.0011315],
	['H1',0.064208],
	['O16',0.035106],
	['Fe54',7.374051999999999e-08],
	['Fe56',1.1575684639999999e-06],
	['Fe57',2.6733304e-08],
	['Fe58',3.5577119999999995e-09]])
# Material Name: 347 stainless steel
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
# Material Name: Water at 27 C
# S(a,b): c_H_in_H2O (Not Implemented)
m3 = mcdc.material(nuclides=[
	['H1',0.066622],
	['O16',0.033311]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=16.5156, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=16.6426, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=46.6426, bc='vacuum')

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
# Space Type: point
mcdc.source(point=[0.0,0.0,0.0], prob=1.0)

mcdc.run()

