import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: UO2F2/D2O Solution
# S(a,b): c_D_in_D2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',7.712e-05],
	['U238',4.3338e-06],
	['F19',0.00016459],
	['O16',0.033159427812],
	['O17',1.2572188000000002e-05],
	['H2',0.065354],
	['H1',0.00066014]])
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
# Material Name: Dry Air
m3 = mcdc.material(nuclides=[
	['N14',3.2150798653e-05],
	['N15',1.1820134700000002e-07],
	['O16',8.6536190349e-06],
	['O17',3.2809650999999998e-09]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=-0.3175, bc='vacuum')
s2 = mcdc.surface('plane-z', z=0.0, bc='interface')
s3 = mcdc.surface('plane-z', z=61.09, bc='interface')
s4 = mcdc.surface('plane-z', z=121.92, bc='interface')
s5 = mcdc.surface('plane-z', z=122.8725, bc='vacuum')
s6 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.1113, bc='interface')
s7 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.27, bc='interface')
s8 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=38.1, bc='interface')
s9 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=38.4175, bc='vacuum')
s10 = mcdc.surface('cylinder-z', center=[21.59, 0.0], radius=1.27, bc='interface')
s11 = mcdc.surface('cylinder-z', center=[21.59, 0.0], radius=1.5875, bc='interface')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s2 & -s9, fill=m2)
c2 = mcdc.cell(+s2 & -s4 & +s8 & -s9, fill=m2)
c3 = mcdc.cell(+s4 & -s5 & +s7 & -s9 & +s11, fill=m2)
c4 = mcdc.cell(+s2 & -s3 & +s7 & -s8 & +s11, fill=m1)
c5 = mcdc.cell(+s3 & -s4 & +s7 & -s8 & +s11, fill=m3)
c6 = mcdc.cell(+s2 & -s5 & -s6, fill=m3)
c7 = mcdc.cell(+s2 & -s5 & +s6 & -s7, fill=m2)
c8 = mcdc.cell(+s2 & -s3 & -s10, fill=m1)
c9 = mcdc.cell(+s3 & -s5 & -s10, fill=m3)
c10 = mcdc.cell(+s2 & -s5 & +s10 & -s11, fill=m2)
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
mcdc.source(point=[0.0,0.0,30.0], prob=1.0)

mcdc.run()

