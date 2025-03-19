import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: UO2F2/D2O Solution
# S(a,b): c_D_in_D2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.0017396999999999998],
	['U238',9.7761e-05],
	['F19',0.0037129],
	['O16',0.033448318281],
	['O17',1.2681718999999998e-05],
	['H2',0.059318],
	['H1',0.00017849]])
# Material Name: 321 Stainless Steel
m2 = mcdc.material(nuclides=[
	['Fe54',0.00346929975],
	['Fe56',0.054460586699999994],
	['Fe57',0.00125773245],
	['Fe58',0.0001673811],
	['Cr50',0.00071740295],
	['Cr52',0.01383440179],
	['Cr53',0.0015687101100000003],
	['Cr54',0.00039048515000000004],
	['Ni58',0.0052557409107],
	['Ni60',0.0020245019893],
	['Ni61',8.80036997e-05],
	['Ni62',0.00028059430350000004],
	['Ni64',7.14590968e-05],
	['Mn55',0.0017363],
	['Si28',0.00156624442576],
	['Si29',7.952942312e-05],
	['Si30',5.242615112e-05]])
# Material Name: Heavy Water
# S(a,b): c_D_in_D2O (Not Implemented)
m3 = mcdc.material(nuclides=[
	['H2',0.066078],
	['H1',0.00039886],
	['O16',0.033225402797999994],
	['O17',1.2597201999999999e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=17.088, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=17.189, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=44.367, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=44.621, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
c3 = mcdc.cell(+s2 & -s3, fill=m3)
c4 = mcdc.cell(+s3 & -s4, fill=m2)
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

