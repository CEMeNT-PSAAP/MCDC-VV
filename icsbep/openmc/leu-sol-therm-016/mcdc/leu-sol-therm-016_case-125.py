import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Uranyl Nitrate Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',9.4999e-05],
	['U238',0.0008461700000000001],
	['H1',0.0578],
	['N14',0.0023658],
	['O16',0.037626734061],
	['O17',1.4265938999999998e-05]])
# Material Name: Stainless steel
m2 = mcdc.material(nuclides=[
	['C0',7.1567e-05],
	['Si28',0.0065865825972],
	['Si29',0.00033444787140000004],
	['Si30',0.00022046953140000003],
	['Mn55',0.0099095],
	['P31',5.0879e-05],
	['S32',9.9070467376e-07],
	['S33',7.80434456e-09],
	['S34',4.373899976e-08],
	['S36',1.5198192e-10],
	['Ni58',0.00582738264],
	['Ni60',0.00224469736],
	['Ni61',9.757543999999999e-05],
	['Ni62',0.00031111320000000003],
	['Ni64',7.923136e-05],
	['Cr50',0.00072670125],
	['Cr52',0.01401371025],
	['Cr53',0.00158904225],
	['Cr54',0.00039554625],
	['Fe54',0.003481282],
	['Fe56',0.05464868240000001],
	['Fe57',0.0012620764000000001],
	['Fe58',0.0001679592]])
# Material Name: Water at 25 C
# S(a,b): c_H_in_H2O (Not Implemented)
m3 = mcdc.material(nuclides=[
	['H1',0.066658],
	['O16',0.033316368309],
	['O17',1.2631690999999998e-05]])
# Material Name: Air
m4 = mcdc.material(nuclides=[
	['N14',3.9016e-05],
	['O16',1.0405054989e-05],
	['O17',3.945011e-09]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-x', x=-67.045, bc='vacuum')
s2 = mcdc.surface('plane-x', x=-37.045, bc='interface')
s3 = mcdc.surface('plane-x', x=-34.515, bc='interface')
s4 = mcdc.surface('plane-x', x=34.515, bc='interface')
s5 = mcdc.surface('plane-x', x=37.045, bc='interface')
s6 = mcdc.surface('plane-x', x=67.045, bc='vacuum')
s11 = mcdc.surface('plane-y', y=-46.57, bc='vacuum')
s12 = mcdc.surface('plane-y', y=-16.57, bc='interface')
s13 = mcdc.surface('plane-y', y=-14.04, bc='interface')
s14 = mcdc.surface('plane-y', y=14.04, bc='interface')
s15 = mcdc.surface('plane-y', y=16.57, bc='interface')
s16 = mcdc.surface('plane-y', y=46.57, bc='vacuum')
s21 = mcdc.surface('plane-z', z=-32.04, bc='vacuum')
s22 = mcdc.surface('plane-z', z=-2.04, bc='interface')
s23 = mcdc.surface('plane-z', z=0.0, bc='interface')
s24 = mcdc.surface('plane-z', z=51.37, bc='interface')
s25 = mcdc.surface('plane-z', z=149.75, bc='interface')
s26 = mcdc.surface('plane-z', z=152.63, bc='interface')
s27 = mcdc.surface('plane-z', z=172.63, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s6 & +s11 & -s16 & +s21 & -s22, fill=m3)
c2 = mcdc.cell(+s3 & -s4 & +s13 & -s14 & +s22 & -s23, fill=m2)
c3 = mcdc.cell(+s3 & -s4 & +s13 & -s14 & +s23 & -s24, fill=m1)
c4 = mcdc.cell(+s3 & -s4 & +s13 & -s14 & +s24 & -s25, fill=m4)
c5 = mcdc.cell(+s3 & -s4 & +s13 & -s14 & +s25 & -s26, fill=m2)
c6 = mcdc.cell(+s2 & -s3 & +s12 & -s15 & +s22 & -s26, fill=m2)
c7 = mcdc.cell(+s3 & -s4 & +s12 & -s13 & +s22 & -s26, fill=m2)
c8 = mcdc.cell(+s3 & -s4 & +s14 & -s15 & +s22 & -s26, fill=m2)
c9 = mcdc.cell(+s4 & -s5 & +s12 & -s15 & +s22 & -s26, fill=m2)
c10 = mcdc.cell(+s1 & -s2 & +s11 & -s16 & +s22 & -s26, fill=m3)
c11 = mcdc.cell(+s2 & -s5 & +s11 & -s12 & +s22 & -s26, fill=m3)
c12 = mcdc.cell(+s2 & -s5 & +s15 & -s16 & +s22 & -s26, fill=m3)
c13 = mcdc.cell(+s5 & -s6 & +s11 & -s16 & +s22 & -s26, fill=m3)
c14 = mcdc.cell(+s1 & -s6 & +s11 & -s16 & +s26 & -s27, fill=m3)
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

