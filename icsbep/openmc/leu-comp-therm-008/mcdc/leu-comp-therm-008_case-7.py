import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Water with 1032.5 PPM Boron
# S(a,b): c_H_in_H2O (Not Implemented)
m1 = mcdc.material(nuclides=[
	['H1',0.066737],
	['O16',0.033369],
	['B10',1.1459e-05],
	['B11',4.6122e-05]])
# Material Name: Fuel (2.459 w/o with B-10 for impurities)
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.00056868],
	['U238',0.022268],
	['O16',0.045682999999999994],
	['B10',2.6055e-07]])
# Material Name: Aluminum 6061 Cladding for Fuel
m3 = mcdc.material(nuclides=[
	['Mg24',0.0004900646472],
	['Mg25',6.219614399999999e-05],
	['Mg26',6.84592088e-05],
	['Al27',0.053985],
	['Si28',0.00029725625863999996],
	['Si29',1.5093824679999998e-05],
	['Si30',9.949916679999998e-06],
	['Ti46',3.8991975e-06],
	['Ti47',3.516367199999999e-06],
	['Ti48',3.48422836e-05],
	['Ti49',2.5569283e-06],
	['Ti50',2.4482234e-06],
	['Cr50',2.5213600500000003e-06],
	['Cr52',4.862191881e-05],
	['Cr53',5.51333529e-06],
	['Cr54',1.3723858500000001e-06],
	['Mn55',4.1191e-05],
	['Fe54',1.1052895e-05],
	['Fe56',0.000173506814],
	['Fe57',4.007029e-06],
	['Fe58',5.33262e-07],
	['Cu63',4.10425995e-05],
	['Cu65',1.8310400499999998e-05],
	['Zn64',2.8360764300000004e-05],
	['Zn66',1.59943867e-05],
	['Zn67',2.3302316e-06],
	['Zn68',1.06417755e-05],
	['Zn70',3.518419e-07]])
# Material Name: Pyrex
m4 = mcdc.material(nuclides=[
	['B10',0.00097491],
	['B11',0.0039241],
	['O16',0.044829],
	['Na23',0.0017444],
	['Al27',0.0010018],
	['Si28',0.0168835652208],
	['Si29',0.0008572992695999999],
	['Si30',0.0005651355095999999]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.514858, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.602996, bc='interface')
s3 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.585, bc='interface')
s4 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.4125, bc='interface')
s5 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.5575, bc='interface')
s6 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.4665, bc='interface')
s7 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.5555, bc='interface')
s99 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=400.0, bc='interface')
s10 = mcdc.surface('plane-z', z=-81.662, bc='vacuum')
s20 = mcdc.surface('plane-z', z=81.662, bc='vacuum')
s30 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=76.2, bc='vacuum')

# Material Cell(s)
c11 = mcdc.cell(-s99, fill=m1)
c12 = mcdc.cell(+s99, fill=m1)
c21 = mcdc.cell(-s1, fill=m2)
c22 = mcdc.cell(+s1 & -s2, fill=m3)
c23 = mcdc.cell(+s2, fill=m1)
c31 = mcdc.cell(-s3, fill=m4)
c32 = mcdc.cell(+s3, fill=m1)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

# Complex Cell(s) Level 1
