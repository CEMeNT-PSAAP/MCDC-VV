import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: fissile solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu238',4.0405e-07],
	['Pu239',0.0008292],
	['Pu240',7.6302e-05],
	['Pu242',4.4252e-07],
	['Gd152',4.81e-08],
	['Gd154',5.242899999999999e-07],
	['Gd155',3.5593999999999998e-06],
	['Gd156',4.923034999999999e-06],
	['Gd157',3.763825e-06],
	['Gd158',5.97402e-06],
	['Gd160',5.257329999999999e-06],
	['H1',0.048973],
	['N14',0.0061360410482000005],
	['N15',2.25589518e-05],
	['O16',0.041712185088],
	['O17',1.5814912e-05]])
# Material Name: 304L stainless steel
m2 = mcdc.material(nuclides=[
	['Fe54',0.0036985991000000004],
	['Fe56',0.05806009612],
	['Fe57',0.0013408608200000001],
	['Fe58',0.00017844395999999998],
	['Cr50',0.0007183154000000001],
	['Cr52',0.01385199748],
	['Cr53',0.0015707053200000004],
	['Cr54',0.00039098180000000005],
	['Ni58',0.0044314658055],
	['Ni60',0.0017069926944999999],
	['Ni61',7.420179049999999e-05],
	['Ni62',0.0002365877775],
	['Ni64',6.0251932e-05]])
# Material Name: Water at 23 C
# S(a,b): c_H_in_H2O (Not Implemented)
m3 = mcdc.material(nuclides=[
	['H1',0.066691],
	['O16',0.033333361866],
	['O17',1.2638134e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s10 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.555, bc='interface')
s11 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.86, bc='interface')
s12 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=30.514, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=30.593, bc='interface')
s14 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=50.523, bc='interface')
s15 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=50.8, bc='vacuum')
s20 = mcdc.surface('plane-z', z=0.0, bc='vacuum')
s21 = mcdc.surface('plane-z', z=0.277, bc='interface')
s22 = mcdc.surface('plane-z', z=21.227, bc='interface')
s23 = mcdc.surface('plane-z', z=22.177, bc='interface')
s24 = mcdc.surface('plane-z', z=51.797, bc='interface')
s25 = mcdc.surface('plane-z', z=127.828, bc='interface')
s26 = mcdc.surface('plane-z', z=127.907, bc='interface')
s27 = mcdc.surface('plane-z', z=143.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s12 & +s23 & -s24, fill=m1)
c2 = mcdc.cell(+s10 & -s15 & +s20 & -s21, fill=m2)
c3 = mcdc.cell(+s10 & -s11 & +s21 & -s22, fill=m2)
c4 = mcdc.cell(-s13 & +s22 & -s23, fill=m2)
c5 = mcdc.cell(+s12 & -s13 & +s23 & -s25, fill=m2)
c6 = mcdc.cell(-s13 & +s25 & -s26, fill=m2)
c7 = mcdc.cell(+s14 & -s15 & +s21 & -s27, fill=m2)
c8 = mcdc.cell(+s11 & -s14 & +s21 & -s22, fill=m3)
c9 = mcdc.cell(+s13 & -s14 & +s22 & -s26, fill=m3)
c10 = mcdc.cell(-s10 & +s20 & -s22, fill=mvoid)
c11 = mcdc.cell(-s12 & +s24 & -s25, fill=mvoid)
c12 = mcdc.cell(-s14 & +s26 & -s27, fill=mvoid)
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

