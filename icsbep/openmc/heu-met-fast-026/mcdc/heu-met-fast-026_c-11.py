import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.044797],
	['U238',0.0026577]])
# Material Name: Stainless Steel
m2 = mcdc.material(nuclides=[
	['C0',0.00031691],
	['Mn55',0.0017320999999999999],
	['Si28',0.0015623707792],
	['Si29',7.93327304e-05],
	['Si30',5.2296490399999995e-05],
	['Cr50',0.0007157084],
	['Cr52',0.013801724080000001],
	['Cr53',0.00156500472],
	['Cr54',0.00038956280000000004],
	['Fe54',0.003528042],
	['Fe56',0.0553827144],
	['Fe57',0.0012790284],
	['Fe58',0.00017021519999999997],
	['Ni58',0.0044136977346],
	['Ni60',0.0017001484654],
	['Ni61',7.39042766e-05],
	['Ni62',0.000235639173],
	['Ni64',6.001035040000001e-05]])
# Material Name: Concrete
m3 = mcdc.material(nuclides=[
	['H1',0.01486568445768],
	['H2',2.31554232e-06],
	['C0',0.0038144000000000003],
	['O16',0.041503264298999996],
	['O17',1.5735701e-05],
	['Na23',0.000304],
	['Mg24',0.00046344237],
	['Mg25',5.88174e-05],
	['Mg26',6.474023e-05],
	['Al27',0.000735],
	['Si28',0.005567905781599999],
	['Si29',0.0002827223692],
	['Si30',0.0001863718492],
	['Ca40',0.01123352308],
	['Ca42',7.497436e-05],
	['Ca43',1.56438e-05],
	['Ca44',0.00024172568],
	['Ca46',4.6352e-07],
	['Ca48',2.166956e-05],
	['Fe54',1.150296e-05],
	['Fe56',0.00018057187200000002],
	['Fe57',4.170192e-06],
	['Fe58',5.549760000000001e-07]])
# Material Name: Paraffin
# S(a,b): c_H_in_CH2 (Not Implemented)
m4 = mcdc.material(nuclides=[
	['H1',0.082574],
	['C0',0.039699]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=5.742, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, -4.2735], radius=0.254, bc='interface')
s3 = mcdc.surface('cylinder-z', center=[0.0, 4.2735], radius=0.254, bc='interface')
s7 = mcdc.surface('plane-z', z=-5.3825, bc='interface')
s8 = mcdc.surface('plane-z', z=5.3825, bc='interface')
s18 = mcdc.surface('plane-x', x=-52.906, bc='interface')
s19 = mcdc.surface('plane-x', x=-45.306, bc='interface')
s20 = mcdc.surface('plane-x', x=-30.458, bc='interface')
s21 = mcdc.surface('plane-x', x=-29.95, bc='interface')
s23 = mcdc.surface('plane-x', x=-0.254, bc='interface')
s24 = mcdc.surface('plane-x', x=0.254, bc='interface')
s26 = mcdc.surface('plane-x', x=29.95, bc='interface')
s27 = mcdc.surface('plane-x', x=30.458, bc='interface')
s28 = mcdc.surface('plane-x', x=45.306, bc='interface')
s29 = mcdc.surface('plane-x', x=52.906, bc='interface')
s12 = mcdc.surface('plane-y', y=-52.906, bc='interface')
s13 = mcdc.surface('plane-y', y=-45.306, bc='interface')
s16 = mcdc.surface('plane-y', y=45.306, bc='interface')
s17 = mcdc.surface('plane-y', y=52.906, bc='interface')
s4 = mcdc.surface('plane-z', z=-51.8275, bc='interface')
s5 = mcdc.surface('plane-z', z=-44.2275, bc='interface')
s10 = mcdc.surface('plane-z', z=44.2275, bc='interface')
s11 = mcdc.surface('plane-z', z=51.8275, bc='interface')
s30 = mcdc.surface('plane-x', x=-496.57, bc='vacuum')
s31 = mcdc.surface('plane-x', x=-344.17, bc='interface')
s32 = mcdc.surface('plane-x', x=554.99, bc='interface')
s33 = mcdc.surface('plane-x', x=600.71, bc='vacuum')
s34 = mcdc.surface('plane-y', y=-624.84, bc='vacuum')
s35 = mcdc.surface('plane-y', y=-563.88, bc='interface')
s36 = mcdc.surface('plane-y', y=-502.92, bc='interface')
s37 = mcdc.surface('plane-y', y=428.96, bc='interface')
s38 = mcdc.surface('plane-y', y=581.36, bc='vacuum')
s39 = mcdc.surface('plane-z', z=-265.3725, bc='vacuum')
s40 = mcdc.surface('plane-z', z=-173.9325, bc='interface')
s41 = mcdc.surface('plane-z', z=191.8275, bc='interface')
s42 = mcdc.surface('plane-z', z=905.5675, bc='interface')
s43 = mcdc.surface('plane-z', z=936.0475, bc='vacuum')

# Material Cell(s)
c10 = mcdc.cell(-s1 & +s2 & +s3 & +s7 & -s8, fill=m1)
c11 = mcdc.cell(-s2 & +s7, fill=m2)
c12 = mcdc.cell(-s3 & +s7, fill=m2)
c13 = mcdc.cell(+s1 & +s7 & -s8, fill=mvoid)
c14 = mcdc.cell(-s7, fill=mvoid)
c15 = mcdc.cell(+s2 & +s3 & +s8, fill=mvoid)
c20 = mcdc.cell(-s1 & +s2 & +s3 & +s7 & -s8, fill=m1)
c21 = mcdc.cell(-s2, fill=m2)
c22 = mcdc.cell(-s3, fill=m2)
c23 = mcdc.cell(+s1 & +s7 & -s8, fill=mvoid)
c24 = mcdc.cell(+s2 & +s3 & -s7, fill=mvoid)
c25 = mcdc.cell(+s2 & +s3 & +s8, fill=mvoid)
c30 = mcdc.cell(-s1 & +s2 & +s3 & +s7 & -s8, fill=m1)
c31 = mcdc.cell(-s2 & -s8, fill=m2)
c32 = mcdc.cell(-s3 & -s8, fill=m2)
c33 = mcdc.cell(+s1 & +s7 & -s8, fill=mvoid)
c34 = mcdc.cell(+s2 & +s3 & -s7, fill=mvoid)
c35 = mcdc.cell(+s8, fill=mvoid)
c40 = mcdc.cell(+s19 & -s20 & +s13 & -s16 & +s4 & -s5, fill=m4)
c41 = mcdc.cell(+s20 & -s21 & +s13 & -s16 & +s4 & -s5, fill=mvoid)
c42 = mcdc.cell(+s21 & -s23 & +s13 & -s16 & +s4 & -s5, fill=m4)
c43 = mcdc.cell(+s23 & -s24 & +s13 & -s16 & +s4 & -s5, fill=mvoid)
c44 = mcdc.cell(+s24 & -s26 & +s13 & -s16 & +s4 & -s5, fill=m4)
c45 = mcdc.cell(+s26 & -s27 & +s13 & -s16 & +s4 & -s5, fill=mvoid)
c46 = mcdc.cell(+s27 & -s28 & +s13 & -s16 & +s4 & -s5, fill=m4)
c47 = mcdc.cell(+s19 & -s20 & +s13 & -s16 & +s10 & -s11, fill=m4)
c48 = mcdc.cell(+s20 & -s21 & +s13 & -s16 & +s10 & -s11, fill=mvoid)
c49 = mcdc.cell(+s21 & -s23 & +s13 & -s16 & +s10 & -s11, fill=m4)
c50 = mcdc.cell(+s23 & -s24 & +s13 & -s16 & +s10 & -s11, fill=mvoid)
c51 = mcdc.cell(+s24 & -s26 & +s13 & -s16 & +s10 & -s11, fill=m4)
c52 = mcdc.cell(+s26 & -s27 & +s13 & -s16 & +s10 & -s11, fill=mvoid)
c53 = mcdc.cell(+s27 & -s28 & +s13 & -s16 & +s10 & -s11, fill=m4)
c54 = mcdc.cell(+s18 & -s29 & +s12 & -s13 & +s4 & -s11, fill=m4)
c55 = mcdc.cell(+s18 & -s29 & +s16 & -s17 & +s4 & -s11, fill=m4)
c56 = mcdc.cell(+s18 & -s19 & +s13 & -s16 & +s4 & -s11, fill=m4)
c57 = mcdc.cell(+s28 & -s29 & +s13 & -s16 & +s4 & -s11, fill=m4)
c80 = mcdc.cell(+s31 & -s32 & +s36 & -s37 & +s40 & -s4, fill=mvoid)
c81 = mcdc.cell(+s31 & -s32 & +s36 & -s12 & +s4 & -s11, fill=mvoid)
c82 = mcdc.cell(+s31 & -s18 & +s12 & -s17 & +s4 & -s11, fill=mvoid)
c83 = mcdc.cell(+s29 & -s32 & +s12 & -s17 & +s4 & -s11, fill=mvoid)
c84 = mcdc.cell(+s31 & -s32 & +s17 & -s37 & +s4 & -s11, fill=mvoid)
c85 = mcdc.cell(+s31 & -s32 & +s36 & -s37 & +s11 & -s41, fill=mvoid)
c86 = mcdc.cell(+s31 & -s32 & +s35 & -s37 & +s41 & -s42, fill=mvoid)
c87 = mcdc.cell(+s30 & -s33 & +s34 & -s38 & +s39 & -s40, fill=m3)
c88 = mcdc.cell(+s30 & -s33 & +s34 & -s36 & +s40 & -s41, fill=m3)
c89 = mcdc.cell(+s30 & -s33 & +s34 & -s35 & +s41 & -s42, fill=m3)
c90 = mcdc.cell(+s30 & -s31 & +s35 & -s36 & +s41 & -s42, fill=m3)
c91 = mcdc.cell(+s32 & -s33 & +s35 & -s36 & +s41 & -s42, fill=m3)
c92 = mcdc.cell(+s30 & -s31 & +s36 & -s37 & +s40 & -s42, fill=m3)
c93 = mcdc.cell(+s32 & -s33 & +s36 & -s37 & +s40 & -s42, fill=m3)
c94 = mcdc.cell(+s30 & -s33 & +s37 & -s38 & +s40 & -s42, fill=m3)
c95 = mcdc.cell(+s30 & -s33 & +s34 & -s38 & +s42 & -s43, fill=m3)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

# Rectangular Lattice 101
Lattice101 = mcdc.lattice(x=[-45.306, 30.204, 3], y=[-45.306, 30.204, 3], z=[-44.2275, 29.485, 3], 