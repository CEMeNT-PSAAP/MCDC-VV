import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Zircaloy-2
m1 = mcdc.material(nuclides=[
	['Zr90',0.0218852865],
	['Zr91',0.004772651399999999],
	['Zr92',0.007295095500000001],
	['Zr94',0.0073929306],
	['Zr96',0.001191036],
	['Sn112',4.842046e-06],
	['Sn114',3.2945879999999994e-06],
	['Sn115',1.697212e-06],
	['Sn116',7.2580772e-05],
	['Sn117',3.8337023999999995e-05],
	['Sn118',0.000120901396],
	['Sn119',4.2879562000000005e-05],
	['Sn120',0.000162632844],
	['Sn122',2.3112034000000005e-05],
	['Sn124',2.8902522e-05]])
# Material Name: Polyethylene (0.9183 g/cm3)
# S(a,b): c_H_in_CH2 (Not Implemented)
m2 = mcdc.material(nuclides=[
	['H1',0.078854],
	['C0',0.039427]])
# Material Name: Water (0.9982 g/cm3)
# S(a,b): c_H_in_H2O (Not Implemented)
m3 = mcdc.material(nuclides=[
	['H1',0.066735],
	['O16',0.033355353528],
	['O17',1.2646472000000002e-05]])
# Material Name: Borated Steel
m4 = mcdc.material(nuclides=[
	['Fe54',0.00346368855],
	['Fe56',0.054372502860000005],
	['Fe57',0.00125569821],
	['Fe58',0.00016711038],
	['Cr50',0.0007572466000000001],
	['Cr52',0.014602746919999998],
	['Cr53',0.0016558342799999999],
	['Cr54',0.00041217219999999994],
	['Mn55',0.00086816],
	['Ni58',0.0051174086499],
	['Ni60',0.0019712166501],
	['Ni61',8.56874229e-05],
	['Ni62',0.0002732089995],
	['Ni64',6.95782776e-05],
	['B10',0.0037488]])
# Material Name: UO2-ZrO2 Seed Fuel (97.29 w/o U-233)
# Depletable
m5 = mcdc.material(nuclides=[
	['U233',0.0039891],
	['U238',4.5759e-05],
	['O16',0.053911559771999996],
	['O17',2.0440228000000005e-05],
	['Zr90',0.011765071499999998],
	['Zr91',0.0025656774],
	['Zr92',0.0039216905],
	['Zr94',0.0039742846],
	['Zr96',0.0006402760000000001]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=42.18, bc='vacuum')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.26797, bc='interface')
s3 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.2794, bc='interface')
s4 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.32385, bc='interface')
s5 = mcdc.surface('plane-z', z=-56.2991, bc='vacuum')
s6 = mcdc.surface('plane-z', z=-25.8191, bc='interface')
s7 = mcdc.surface('plane-z', z=-19.05, bc='interface')
s8 = mcdc.surface('plane-z', z=16.05, bc='interface')
s9 = mcdc.surface('plane-z', z=19.05, bc='interface')
s10 = mcdc.surface('plane-z', z=25.8191, bc='interface')
s11 = mcdc.surface('plane-z', z=56.2991, bc='vacuum')
s12 = mcdc.surface('plane-x', x=-8.27532, bc='interface')
s13 = mcdc.surface('plane-x', x=8.27532, bc='interface')
s14 = mcdc.surface('plane-y', y=-7.35584, bc='interface')
s15 = mcdc.surface('plane-y', y=7.35584, bc='interface')
s21 = mcdc.surface('plane-x', x=-0.37084, bc='interface')
s22 = mcdc.surface('plane-x', x=0.37084, bc='interface')
s23 = mcdc.surface('plane-y', y=-0.37084, bc='interface')
s24 = mcdc.surface('plane-y', y=0.37084, bc='interface')
s25 = mcdc.surface('plane-x', x=-3.81, bc='interface')
s26 = mcdc.surface('plane-x', x=3.81, bc='interface')
s27 = mcdc.surface('plane-y', y=-5.60578, bc='interface')
s28 = mcdc.surface('plane-y', y=-5.42798, bc='interface')
s29 = mcdc.surface('plane-y', y=-1.92786, bc='interface')
s30 = mcdc.surface('plane-y', y=-1.75006, bc='interface')
s31 = mcdc.surface('plane-y', y=1.75006, bc='interface')
s32 = mcdc.surface('plane-y', y=1.92786, bc='interface')
s33 = mcdc.surface('plane-y', y=5.42798, bc='interface')
s34 = mcdc.surface('plane-y', y=5.60578, bc='interface')

# Material Cell(s)
c101 = mcdc.cell(-s2 & +s7 & -s9, fill=m5)
c102 = mcdc.cell(-s2 & -s7, fill=m1)
c103 = mcdc.cell(-s2 & +s9, fill=m1)
c104 = mcdc.cell(+s2 & -s3, fill=mvoid)
c105 = mcdc.cell(+s3 & -s4, fill=m1)
c106 = mcdc.cell(+s4, fill=m3)
c201 = mcdc.cell(-s2 & +s7 & -s9, fill=m5)
c202 = mcdc.cell(-s2 & -s7, fill=m1)
c203 = mcdc.cell(-s2 & +s9, fill=m1)
c204 = mcdc.cell(+s2 & -s3, fill=mvoid)
c205 = mcdc.cell(+s3 & -s4, fill=m1)
c206 = mcdc.cell(+s4 & -s8, fill=m3)
c207 = mcdc.cell(+s4 & +s8 & +s23, fill=m3)
c208 = mcdc.cell(+s8 & -s23, fill=m4)
c301 = mcdc.cell(-s2 & +s7 & -s9, fill=m5)
c302 = mcdc.cell(-s2 & -s7, fill=m1)
c303 = mcdc.cell(-s2 & +s9, fill=m1)
c304 = mcdc.cell(+s2 & -s3, fill=mvoid)
c305 = mcdc.cell(+s3 & -s4, fill=m1)
c306 = mcdc.cell(+s4 & -s8, fill=m3)
c307 = mcdc.cell(+s4 & +s8 & -s24, fill=m3)
c308 = mcdc.cell(+s8 & +s24, fill=m4)
c401 = mcdc.cell(-s2 & +s7 & -s9, fill=m5)
c402 = mcdc.cell(-s2 & -s7, fill=m1)
c403 = mcdc.cell(-s2 & +s9, fill=m1)
c404 = mcdc.cell(+s2 & -s3, fill=mvoid)
c405 = mcdc.cell(+s3 & -s4, fill=m1)
c406 = mcdc.cell(+s4 & -s8, fill=m3)
c407 = mcdc.cell(+s4 & +s8 & +s23, fill=m3)
c408 = mcdc.cell(+s4 & +s8 & -s23 & -s22, fill=m3)
c409 = mcdc.cell(+s8 & -s23 & +s22, fill=m4)
c501 = mcdc.cell(-s2 & +s7 & -s9, fill=m5)
c502 = mcdc.cell(-s2 & -s7, fill=m1)
c503 = mcdc.cell(-s2 & +s9, fill=m1)
c504 = mcdc.cell(+s2 & -s3, fill=mvoid)
c505 = mcdc.cell(+s3 & -s4, fill=m1)
c506 = mcdc.cell(+s4 & -s8, fill=m3)
c507 = mcdc.cell(+s4 & +s8 & +s23, fill=m3)
c508 = mcdc.cell(+s4 & +s8 & -s23 & +s21, fill=m3)
c509 = mcdc.cell(+s8 & -s23 & -s21, fill=m4)
c601 = mcdc.cell(-s2 & +s7 & -s9, fill=m5)
c602 = mcdc.cell(-s2 & -s7, fill=m1)
c603 = mcdc.cell(-s2 & +s9, fill=m1)
c604 = mcdc.cell(+s2 & -s3, fill=mvoid)
c605 = mcdc.cell(+s3 & -s4, fill=m1)
c606 = mcdc.cell(+s4 & -s8, fill=m3)
c607 = mcdc.cell(+s4 & +s8 & -s24, fill=m3)
c608 = mcdc.cell(+s4 & +s8 & +s24 & -s22, fill=m3)
c609 = mcdc.cell(+s8 & +s24 & +s22, fill=m4)
c701 = mcdc.cell(-s2 & +s7 & -s9, fill=m5)
c702 = mcdc.cell(-s2 & -s7, fill=m1)
c703 = mcdc.cell(-s2 & +s9, fill=m1)
c704 = mcdc.cell(+s2 & -s3, fill=mvoid)
c705 = mcdc.cell(+s3 & -s4, fill=m1)
c706 = mcdc.cell(+s4 & -s8, fill=m3)
c707 = mcdc.cell(+s4 & +s8 & -s24, fill=m3)
c708 = mcdc.cell(+s4 & +s8 & +s24 & +s21, fill=m3)
c709 = mcdc.cell(+s8 & +s24 & -s21, fill=m4)
c7 = mcdc.cell(+s10 & -s11 & +s25 & -s26 & +s27 & -s28, fill=m4)
c8 = mcdc.cell(+s10 & -s11 & +s25 & -s26 & +s29 & -s30, fill=m4)
c9 = mcdc.cell(+s10 & -s11 & +s25 & -s26 & +s31 & -s32, fill=m4)
c10 = mcdc.cell(+s10 & -s11 & +s25 & -s26 & +s33 & -s34, fill=m4)
c14 = mcdc.cell(-s1 & +s5 & -s6, fill=m3)
c15 = mcdc.cell(-s1 & +s6 & -s10 & -s12, fill=m3)
c16 = mcdc.cell(-s1 & +s6 & -s10 & +s13, fill=m3)
c17 = mcdc.cell(-s1 & +s6 & -s10 & +s12 & -s13 & -s14, fill=m3)
c18 = mcdc.cell(-s1 & +s6 & -s10 & +s12 & -s13 & +s15, fill=m3)
c19 = mcdc.cell(-s1 & +s10 & -s11 & -s27, fill=m3)
c20 = mcdc.cell(-s1 & +s10 & -s11 & +s27 & -s28 & -s25, fill=m3)
c21 = mcdc.cell(-s1 & +s10 & -s11 & +s27 & -s28 & +s26, fill=m3)
c22 = mcdc.cell(-s1 & +s10 & -s11 & +s28 & -s29, fill=m3)
c23 = mcdc.cell(-s1 & +s10 & -s11 & +s29 & -s30 & -s25, fill=m3)
c24 = mcdc.cell(-s1 & +s10 & -s11 & +s29 & -s30 & +s26, fill=m3)
c25 = mcdc.cell(-s1 & +s10 & -s11 & +s30 & -s31, fill=m3)
c26 = mcdc.cell(-s1 & +s10 & -s11 & +s31 & -s32 & -s25, fill=m3)
c27 = mcdc.cell(-s1 & +s10 & -s11 & +s31 & -s32 & +s26, fill=m3)
c28 = mcdc.cell(-s1 & +s10 & -s11 & +s32 & -s33, fill=m3)
c29 = mcdc.cell(-s1 & +s10 & -s11 & +s33 & -s34 & -s25, fill=m3)
c30 = mcdc.cell(-s1 & +s10 & -s11 & +s33 & -s34 & +s26, fill=m3)
c31 = mcdc.cell(-s1 & +s10 & -s11 & +s34, fill=m3)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

# Rectangular Lattice 100
Lattice100 = mcdc.lattice(x=[-8.27532, 0.91948, 18], y=[-7.35584, 0.91948, 16], 