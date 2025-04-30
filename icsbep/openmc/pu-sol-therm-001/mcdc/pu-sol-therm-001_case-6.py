import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium nitrate solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu238',4.0785e-08],
	['Pu239',0.00064313],
	['Pu240',3.1466e-05],
	['Pu242',6.0164e-08],
	['N14',0.0033692],
	['H1',0.058646],
	['O16',0.039099]])
# Material Name: Stainless steel
m2 = mcdc.material(nuclides=[
	['Fe54',0.00346929975],
	['Fe56',0.0544605867],
	['Fe57',0.00125773245],
	['Fe58',0.0001673811],
	['Cr50',0.0007572465999999999],
	['Cr52',0.014602746920000001],
	['Cr53',0.0016558342799999999],
	['Cr54',0.0004121722],
	['Ni58',0.0052557409107],
	['Ni60',0.0020245019893],
	['Ni61',8.800369969999998e-05],
	['Ni62',0.00028059430350000004],
	['Ni64',7.14590968e-05],
	['Mn55',0.0017363]])
# Material Name: Water at 25 C
# S(a,b): c_H_in_H2O (Not Implemented)
m3 = mcdc.material(nuclides=[
	['H1',0.066655],
	['O16',0.033327]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=14.5189, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=14.6434, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=44.6434, bc='vacuum')

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

