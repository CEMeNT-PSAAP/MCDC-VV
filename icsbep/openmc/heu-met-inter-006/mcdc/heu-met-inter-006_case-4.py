import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.044949],
	['U238',0.0025779]])
# Material Name: c_Graphite
# S(a,b): c_Graphite (Not Implemented)
m2 = mcdc.material(nuclides=[
	['C0',0.086552]])
# Material Name: Cu
m3 = mcdc.material(nuclides=[
	['Cu63',0.05724237000000001],
	['Cu65',0.025537630000000002]])
# Material Name: Al 6061-T6
m4 = mcdc.material(nuclides=[
	['Si28',0.00031630168756000004],
	['Si29',1.6060897220000002e-05],
	['Si30',1.058741522e-05],
	['Fe54',5.8806545e-06],
	['Fe56',9.23136994e-05],
	['Fe57',2.1319259000000002e-06],
	['Fe58',2.837202e-07],
	['Cu63',4.80391965e-05],
	['Cu65',2.14318035e-05],
	['Mn55',2.1915e-05],
	['Mg24',0.0005214634599],
	['Mg25',6.6181098e-05],
	['Mg26',7.28454421e-05],
	['Cr50',3.35368825e-06],
	['Cr52',6.467253965e-05],
	['Cr53',7.33334685e-06],
	['Cr54',1.82542525e-06],
	['Zn64',1.5088797899999998e-05],
	['Zn66',8.509505099999999e-06],
	['Zn67',1.2397548e-06],
	['Zn68',5.6617514999999996e-06],
	['Zn70',1.871907e-07],
	['Ti46',2.074545e-06],
	['Ti47',1.8708623999999995e-06],
	['Ti48',1.8537631199999998e-05],
	['Ti49',1.3603986e-06],
	['Ti50',1.3025628e-06],
	['Al27',0.057816]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=-5.7912, bc='vacuum')
s2 = mcdc.surface('plane-z', z=0.0, bc='interface')
s3 = mcdc.surface('plane-z', z=29.98828, bc='interface')
s4 = mcdc.surface('plane-z', z=36.33828, bc='interface')
s5 = mcdc.surface('plane-z', z=50.76548, bc='interface')
s6 = mcdc.surface('plane-z', z=51.77284, bc='interface')
s7 = mcdc.surface('plane-z', z=52.07256, bc='interface')
s8 = mcdc.surface('plane-z', z=53.07992, bc='interface')
s9 = mcdc.surface('plane-z', z=54.08728, bc='interface')
s10 = mcdc.surface('plane-z', z=54.387, bc='interface')
s11 = mcdc.surface('plane-z', z=55.39436, bc='interface')
s12 = mcdc.surface('plane-z', z=56.40172, bc='interface')
s13 = mcdc.surface('plane-z', z=56.70144, bc='interface')
s14 = mcdc.surface('plane-z', z=57.7088, bc='interface')
s15 = mcdc.surface('plane-z', z=58.71616, bc='interface')
s16 = mcdc.surface('plane-z', z=59.01588, bc='interface')
s17 = mcdc.surface('plane-z', z=60.02324, bc='interface')
s18 = mcdc.surface('plane-z', z=61.0306, bc='interface')
s19 = mcdc.surface('plane-z', z=61.33032, bc='interface')
s20 = mcdc.surface('plane-z', z=62.33768, bc='interface')
s21 = mcdc.surface('plane-z', z=63.34504, bc='interface')
s22 = mcdc.surface('plane-z', z=63.64476, bc='interface')
s23 = mcdc.surface('plane-z', z=64.65212, bc='interface')
s24 = mcdc.surface('plane-z', z=65.65948, bc='interface')
s25 = mcdc.surface('plane-z', z=65.9592, bc='interface')
s26 = mcdc.surface('plane-z', z=66.96656, bc='interface')
s27 = mcdc.surface('plane-z', z=67.97392, bc='interface')
s28 = mcdc.surface('plane-z', z=68.27364, bc='interface')
s29 = mcdc.surface('plane-z', z=69.281, bc='interface')
s30 = mcdc.surface('plane-z', z=70.28836, bc='interface')
s31 = mcdc.surface('plane-z', z=70.58808, bc='interface')
s32 = mcdc.surface('plane-z', z=71.59544, bc='interface')
s33 = mcdc.surface('plane-z', z=71.83755, bc='interface')
s34 = mcdc.surface('plane-z', z=86.26475, bc='interface')
s35 = mcdc.surface('plane-z', z=123.9012, bc='vacuum')
s36 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.54, bc='interface')
s37 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.1496, bc='interface')
s38 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.175, bc='interface')
s39 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=4.7625, bc='interface')
s40 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=19.05, bc='interface')
s41 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=26.67, bc='interface')
s42 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=26.797, bc='interface')
s43 = mcdc.surface('plane-x', x=-44.1452, bc='vacuum')
s44 = mcdc.surface('plane-x', x=-27.94, bc='interface')
s45 = mcdc.surface('plane-x', x=27.94, bc='interface')
s46 = mcdc.surface('plane-x', x=44.1452, bc='vacuum')
s47 = mcdc.surface('plane-y', y=-44.1452, bc='vacuum')
s48 = mcdc.surface('plane-y', y=-27.94, bc='interface')
s49 = mcdc.surface('plane-y', y=27.94, bc='interface')
s50 = mcdc.surface('plane-y', y=44.1452, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s14 & -s36, fill=mvoid)
c2 = mcdc.cell(+s1 & -s14 & +s36 & -s37, fill=m4)
c3 = mcdc.cell(+s1 & -s14 & +s37 & -s38, fill=mvoid)
c4 = mcdc.cell(+s1 & -s2 & +s38 & +s43 & -s46 & +s47 & -s50, fill=mvoid)
c5 = mcdc.cell(+s2 & -s3 & +s38 & -s41, fill=mvoid)
c6 = mcdc.cell(+s3 & -s4 & +s38 & -s39, fill=mvoid)
c7 = mcdc.cell(+s3 & -s4 & +s39 & -s41, fill=m4)
c8 = mcdc.cell(+s4 & -s5 & +s38 & -s41, fill=m3)
c9 = mcdc.cell(+s5 & -s6 & +s38 & -s41, fill=m2)
c10 = mcdc.cell(+s6 & -s7 & +s38 & -s40, fill=m1)
c11 = mcdc.cell(+s6 & -s7 & +s40 & -s41, fill=mvoid)
c12 = mcdc.cell(+s7 & -s8 & +s38 & -s41, fill=m2)
c13 = mcdc.cell(+s8 & -s9 & +s38 & -s41, fill=m2)
c14 = mcdc.cell(+s9 & -s10 & +s38 & -s41, fill=m1)
c15 = mcdc.cell(+s10 & -s11 & +s38 & -s41, fill=m2)
c16 = mcdc.cell(+s11 & -s12 & +s38 & -s41, fill=m2)
c17 = mcdc.cell(+s12 & -s13 & +s38 & -s41, fill=m1)
c18 = mcdc.cell(+s13 & -s14 & +s38 & -s41, fill=m2)
c19 = mcdc.cell(+s14 & -s15 & -s41, fill=m2)
c20 = mcdc.cell(+s15 & -s16 & -s41, fill=m1)
c21 = mcdc.cell(+s16 & -s17 & -s41, fill=m2)
c22 = mcdc.cell(+s17 & -s18 & -s41, fill=m2)
c23 = mcdc.cell(+s18 & -s19 & -s41, fill=m1)
c24 = mcdc.cell(+s19 & -s20 & -s41, fill=m2)
c25 = mcdc.cell(+s20 & -s21 & -s41, fill=m2)
c26 = mcdc.cell(+s21 & -s22 & -s41, fill=m1)
c27 = mcdc.cell(+s22 & -s23 & -s41, fill=m2)
c28 = mcdc.cell(+s23 & -s24 & -s41, fill=m2)
c29 = mcdc.cell(+s24 & -s25 & -s41, fill=m1)
c30 = mcdc.cell(+s25 & -s26 & -s41, fill=m2)
c31 = mcdc.cell(+s26 & -s27 & -s41, fill=m2)
c32 = mcdc.cell(+s27 & -s28 & -s41, fill=m1)
c33 = mcdc.cell(+s28 & -s29 & -s41, fill=m2)
c34 = mcdc.cell(+s29 & -s30 & -s41, fill=m2)
c35 = mcdc.cell(+s30 & -s31 & -s41, fill=m1)
c36 = mcdc.cell(+s31 & -s32 & -s41, fill=m2)
c37 = mcdc.cell(+s32 & -s33 & -s41, fill=mvoid)
c38 = mcdc.cell(+s33 & -s34 & -s42, fill=m3)
c39 = mcdc.cell(+s34 & -s35 & +s44 & -s45 & +s48 & -s49, fill=mvoid)
c40 = mcdc.cell(+s34 & -s35 & +s43 & -s44 & +s47 & -s50, fill=m3)
c41 = mcdc.cell(+s34 & -s35 & +s45 & -s46 & +s47 & -s50, fill=m3)
c42 = mcdc.cell(+s34 & -s35 & +s44 & -s45 & +s47 & -s48, fill=m3)
c43 = mcdc.cell(+s34 & -s35 & +s44 & -s45 & +s49 & -s50, fill=m3)
c44 = mcdc.cell(+s2 & -s33 & +s41 & -s42, fill=mvoid)
c45 = mcdc.cell(+s2 & -s34 & +s42 & +s43 & -s46 & +s47 & -s50, fill=m3)
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
mcdc.source(x=[-0.5,0.5], y=[-0.5,0.5], z=[57.2,57.7], prob=1.0)

mcdc.run()

