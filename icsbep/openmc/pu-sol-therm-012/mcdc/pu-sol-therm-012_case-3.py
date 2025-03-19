import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium nitrate solution (16.7 g/L)
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',3.12659e-05],
	['Pu240',7.92231e-06],
	['Pu242',4.7438800000000005e-07],
	['Am241',2.54492e-07],
	['N14',0.00138024557284],
	['N15',5.07442716e-06],
	['O16',0.0353632922307],
	['O17',1.3407769299999999e-05],
	['H1',0.0636398],
	['Fe54',2.39505889e-07],
	['Fe56',3.7597302548e-06],
	['Fe57',8.682856780000001e-08],
	['Fe58',1.1555288400000001e-08],
	['Cr50',5.7254065e-08],
	['Cr52',1.104087653e-06],
	['Cr53',1.25194677e-07],
	['Cr54',3.1163605e-08],
	['Ni58',6.35785826787e-07],
	['Ni60',2.4490356221299997e-07],
	['Ni61',1.0645788276999998e-08],
	['Ni62',3.3943431435e-08],
	['Ni64',8.644391288e-09]])
# Material Name: Air
m2 = mcdc.material(nuclides=[
	['O16',1.0784e-05],
	['N14',4.309e-05]])
# Material Name: Stainless steel
m3 = mcdc.material(nuclides=[
	['Fe54',0.003585556800000001],
	['Fe56',0.056285573760000006],
	['Fe57',0.0012998793600000002],
	['Fe58',0.00017299008000000001],
	['Cr50',0.0007157084],
	['Cr52',0.013801724080000001],
	['Cr53',0.00156500472],
	['Cr54',0.00038956280000000004],
	['Ni58',0.005517632744999999],
	['Ni60',0.0021253822549999997],
	['Ni61',9.2388895e-05],
	['Ni62',0.000294576225],
	['Ni64',7.501988e-05]])
# Material Name: Lucoflex
m4 = mcdc.material(nuclides=[
	['C0',0.027365],
	['H1',0.041047],
	['Cl35',0.010366126253999998],
	['Cl37',0.0033158737460000005]])
# Material Name: Water
# S(a,b): c_H_in_H2O (Not Implemented)
m5 = mcdc.material(nuclides=[
	['H1',0.066688],
	['O16',0.033331362624],
	['O17',1.2637376e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-x', x=-90.5, bc='vacuum')
s2 = mcdc.surface('plane-x', x=-65.5, bc='interface')
s3 = mcdc.surface('plane-x', x=-65.0, bc='interface')
s4 = mcdc.surface('plane-x', x=-64.0, bc='interface')
s5 = mcdc.surface('plane-x', x=64.0, bc='interface')
s6 = mcdc.surface('plane-x', x=65.0, bc='interface')
s7 = mcdc.surface('plane-x', x=65.5, bc='interface')
s8 = mcdc.surface('plane-x', x=90.5, bc='vacuum')
s11 = mcdc.surface('plane-y', y=-90.5, bc='vacuum')
s12 = mcdc.surface('plane-y', y=-65.5, bc='interface')
s13 = mcdc.surface('plane-y', y=-65.0, bc='interface')
s14 = mcdc.surface('plane-y', y=-64.0, bc='interface')
s15 = mcdc.surface('plane-y', y=64.0, bc='interface')
s16 = mcdc.surface('plane-y', y=65.0, bc='interface')
s17 = mcdc.surface('plane-y', y=65.5, bc='interface')
s18 = mcdc.surface('plane-y', y=90.5, bc='vacuum')
s21 = mcdc.surface('plane-z', z=-25.5, bc='vacuum')
s22 = mcdc.surface('plane-z', z=-0.5, bc='interface')
s23 = mcdc.surface('plane-z', z=0.0, bc='interface')
s24 = mcdc.surface('plane-z', z=35.44, bc='interface')
s25 = mcdc.surface('plane-z', z=36.44, bc='interface')
s26 = mcdc.surface('plane-z', z=54.44, bc='interface')
s27 = mcdc.surface('plane-z', z=55.44, bc='interface')
s28 = mcdc.surface('plane-z', z=100.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s3 & -s6 & +s13 & -s16 & +s23 & -s24, fill=m1)
c10 = mcdc.cell(+s2 & -s7 & +s12 & -s17 & +s22 & -s23, fill=m3)
c11 = mcdc.cell(+s2 & -s3 & +s12 & -s17 & +s23 & -s28, fill=m3)
c12 = mcdc.cell(+s3 & -s6 & +s12 & -s13 & +s23 & -s28, fill=m3)
c13 = mcdc.cell(+s3 & -s6 & +s16 & -s17 & +s23 & -s28, fill=m3)
c14 = mcdc.cell(+s6 & -s7 & +s12 & -s17 & +s23 & -s28, fill=m3)
c20 = mcdc.cell(+s3 & -s6 & +s13 & -s16 & +s24 & -s25, fill=m4)
c21 = mcdc.cell(+s3 & -s4 & +s13 & -s16 & +s25 & -s26, fill=m4)
c22 = mcdc.cell(+s4 & -s5 & +s13 & -s14 & +s25 & -s26, fill=m4)
c23 = mcdc.cell(+s4 & -s5 & +s15 & -s16 & +s25 & -s26, fill=m4)
c24 = mcdc.cell(+s5 & -s6 & +s13 & -s16 & +s25 & -s26, fill=m4)
c25 = mcdc.cell(+s3 & -s6 & +s13 & -s16 & +s26 & -s27, fill=m4)
c26 = mcdc.cell(+s4 & -s5 & +s14 & -s15 & +s25 & -s26, fill=m5)
c27 = mcdc.cell(+s3 & -s6 & +s13 & -s16 & +s27 & -s28, fill=m2)
c30 = mcdc.cell(+s1 & -s8 & +s11 & -s18 & +s21 & -s22, fill=m5)
c31 = mcdc.cell(+s1 & -s2 & +s11 & -s18 & +s22 & -s27, fill=m5)
c32 = mcdc.cell(+s2 & -s7 & +s11 & -s12 & +s22 & -s27, fill=m5)
c33 = mcdc.cell(+s2 & -s7 & +s17 & -s18 & +s22 & -s27, fill=m5)
c34 = mcdc.cell(+s7 & -s8 & +s11 & -s18 & +s22 & -s27, fill=m5)
c35 = mcdc.cell(+s1 & -s2 & +s11 & -s18 & +s27 & -s28, fill=m2)
c36 = mcdc.cell(+s2 & -s7 & +s11 & -s12 & +s27 & -s28, fill=m2)
c37 = mcdc.cell(+s2 & -s7 & +s17 & -s18 & +s27 & -s28, fill=m2)
c38 = mcdc.cell(+s7 & -s8 & +s11 & -s18 & +s27 & -s28, fill=m2)
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
mcdc.source(x=[-65.0,65.0], y=[-65.0,65.0], z=[0.0,23.0], prob=1.0)

mcdc.run()

