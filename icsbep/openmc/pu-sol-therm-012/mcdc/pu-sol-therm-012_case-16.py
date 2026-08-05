import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium nitrate solution (26.9 g/L)
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',5.03642e-05],
	['Pu240',1.27611e-05],
	['Pu242',7.641340000000001e-07],
	['Am241',4.09931e-07],
	['N14',0.0015229409579800002],
	['N15',5.5990420200000005e-06],
	['O16',0.0354792482667],
	['O17',1.34517333e-05],
	['H1',0.0630426],
	['Fe54',3.718641605e-07],
	['Fe56',5.8374720586e-06],
	['Fe57',1.348126871e-07],
	['Fe58',1.79410938e-08],
	['Cr50',8.889435500000002e-08],
	['Cr52',1.714239151e-06],
	['Cr53',1.9438095900000004e-07],
	['Cr54',4.838553500000001e-08],
	['Ni58',9.8714228076e-07],
	['Ni60',3.8024543923999996e-07],
	['Ni61',1.6529005959999998e-08],
	['Ni62',5.27017038e-08],
	['Ni64',1.3421570239999999e-08]])
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
# Material Name: Steel (pool wall)
m6 = mcdc.material(nuclides=[
	['Fe54',0.0049722246],
	['Fe56',0.07805329272],
	['Fe57',0.0018025909200000002],
	['Fe58',0.00023989176000000002],
	['C0',0.00055545]])
# Material Name: Concrete
m7 = mcdc.material(nuclides=[
	['H1',0.010349999999999998],
	['B10',1.6020000000000003e-06],
	['O16',0.04345352487],
	['O17',1.647513e-05],
	['Al27',0.001563],
	['Si28',0.013068945656000001],
	['Si29',0.0006636037720000001],
	['Si30',0.00043745057199999997],
	['Ca40',0.00622748984],
	['Ca42',4.156328000000001e-05],
	['Ca43',8.6724e-06],
	['Ca44',0.00013400464],
	['Ca46',2.5696000000000005e-07],
	['Ca48',1.201288e-05],
	['Fe54',4.4544745000000004e-05],
	['Fe56',0.0006992572339999999],
	['Fe57',1.6148899e-05],
	['Fe58',2.149122e-06]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-x', x=-105.0, bc='interface')
s2 = mcdc.surface('plane-x', x=-65.5, bc='interface')
s3 = mcdc.surface('plane-x', x=-65.0, bc='interface')
s4 = mcdc.surface('plane-x', x=-64.0, bc='interface')
s5 = mcdc.surface('plane-x', x=64.0, bc='interface')
s6 = mcdc.surface('plane-x', x=65.0, bc='interface')
s7 = mcdc.surface('plane-x', x=65.5, bc='interface')
s8 = mcdc.surface('plane-x', x=105.0, bc='interface')
s31 = mcdc.surface('plane-x', x=-655.0, bc='vacuum')
s32 = mcdc.surface('plane-x', x=-605.0, bc='interface')
s33 = mcdc.surface('plane-x', x=-105.8, bc='interface')
s34 = mcdc.surface('plane-x', x=105.8, bc='interface')
s35 = mcdc.surface('plane-x', x=605.0, bc='interface')
s36 = mcdc.surface('plane-x', x=655.0, bc='vacuum')
s11 = mcdc.surface('plane-y', y=-160.0, bc='interface')
s12 = mcdc.surface('plane-y', y=-65.5, bc='interface')
s13 = mcdc.surface('plane-y', y=-65.0, bc='interface')
s14 = mcdc.surface('plane-y', y=-64.0, bc='interface')
s15 = mcdc.surface('plane-y', y=64.0, bc='interface')
s16 = mcdc.surface('plane-y', y=65.0, bc='interface')
s17 = mcdc.surface('plane-y', y=65.5, bc='interface')
s18 = mcdc.surface('plane-y', y=160.0, bc='interface')
s41 = mcdc.surface('plane-y', y=-490.0, bc='vacuum')
s42 = mcdc.surface('plane-y', y=-440.0, bc='interface')
s43 = mcdc.surface('plane-y', y=-160.8, bc='interface')
s44 = mcdc.surface('plane-y', y=160.8, bc='interface')
s45 = mcdc.surface('plane-y', y=440.0, bc='interface')
s46 = mcdc.surface('plane-y', y=490.0, bc='vacuum')
s21 = mcdc.surface('plane-z', z=-50.5, bc='interface')
s22 = mcdc.surface('plane-z', z=-0.5, bc='interface')
s23 = mcdc.surface('plane-z', z=0.0, bc='interface')
s24 = mcdc.surface('plane-z', z=24.76, bc='interface')
s25 = mcdc.surface('plane-z', z=80.0, bc='interface')
s26 = mcdc.surface('plane-z', z=81.0, bc='interface')
s27 = mcdc.surface('plane-z', z=99.0, bc='interface')
s28 = mcdc.surface('plane-z', z=100.0, bc='interface')
s51 = mcdc.surface('plane-z', z=-103.3, bc='vacuum')
s52 = mcdc.surface('plane-z', z=-63.3, bc='interface')
s53 = mcdc.surface('plane-z', z=-51.3, bc='interface')
s54 = mcdc.surface('plane-z', z=936.7, bc='interface')
s55 = mcdc.surface('plane-z', z=986.7, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s3 & -s6 & +s13 & -s16 & +s23 & -s24, fill=m1)
c2 = mcdc.cell(+s3 & -s6 & +s13 & -s16 & +s24 & -s25, fill=m2)
c10 = mcdc.cell(+s2 & -s7 & +s12 & -s17 & +s22 & -s23, fill=m3)
c11 = mcdc.cell(+s2 & -s3 & +s12 & -s17 & +s23 & -s28, fill=m3)
c12 = mcdc.cell(+s3 & -s6 & +s12 & -s13 & +s23 & -s28, fill=m3)
c13 = mcdc.cell(+s3 & -s6 & +s16 & -s17 & +s23 & -s28, fill=m3)
c14 = mcdc.cell(+s6 & -s7 & +s12 & -s17 & +s23 & -s28, fill=m3)
c20 = mcdc.cell(+s3 & -s6 & +s13 & -s16 & +s25 & -s26, fill=m4)
c21 = mcdc.cell(+s3 & -s4 & +s13 & -s16 & +s26 & -s27, fill=m4)
c22 = mcdc.cell(+s4 & -s5 & +s13 & -s14 & +s26 & -s27, fill=m4)
c23 = mcdc.cell(+s4 & -s5 & +s15 & -s16 & +s26 & -s27, fill=m4)
c24 = mcdc.cell(+s5 & -s6 & +s13 & -s16 & +s26 & -s27, fill=m4)
c25 = mcdc.cell(+s3 & -s6 & +s13 & -s16 & +s27 & -s28, fill=m4)
c26 = mcdc.cell(+s4 & -s5 & +s14 & -s15 & +s26 & -s27, fill=m2)
c30 = mcdc.cell(+s1 & -s8 & +s11 & -s18 & +s21 & -s22, fill=m2)
c31 = mcdc.cell(+s1 & -s2 & +s11 & -s18 & +s22 & -s28, fill=m2)
c32 = mcdc.cell(+s2 & -s7 & +s11 & -s12 & +s22 & -s28, fill=m2)
c33 = mcdc.cell(+s2 & -s7 & +s17 & -s18 & +s22 & -s28, fill=m2)
c34 = mcdc.cell(+s7 & -s8 & +s11 & -s18 & +s22 & -s28, fill=m2)
c41 = mcdc.cell(+s31 & -s36 & +s41 & -s46 & +s51 & -s52, fill=m7)
c42 = mcdc.cell(+s31 & -s32 & +s41 & -s46 & +s52 & -s54, fill=m7)
c43 = mcdc.cell(+s32 & -s35 & +s41 & -s42 & +s52 & -s54, fill=m7)
c44 = mcdc.cell(+s32 & -s35 & +s45 & -s46 & +s52 & -s54, fill=m7)
c45 = mcdc.cell(+s35 & -s36 & +s41 & -s46 & +s52 & -s54, fill=m7)
c46 = mcdc.cell(+s31 & -s36 & +s41 & -s46 & +s54 & -s55, fill=m7)
c51 = mcdc.cell(+s32 & -s35 & +s42 & -s45 & +s52 & -s53, fill=m2)
c52 = mcdc.cell(+s32 & -s33 & +s42 & -s45 & +s53 & -s28, fill=m2)
c53 = mcdc.cell(+s33 & -s34 & +s42 & -s43 & +s53 & -s28, fill=m2)
c54 = mcdc.cell(+s33 & -s34 & +s44 & -s45 & +s53 & -s28, fill=m2)
c55 = mcdc.cell(+s34 & -s35 & +s42 & -s45 & +s53 & -s28, fill=m2)
c56 = mcdc.cell(+s32 & -s35 & +s42 & -s45 & +s28 & -s54, fill=m2)
c61 = mcdc.cell(+s33 & -s34 & +s43 & -s44 & +s53 & -s21, fill=m6)
c62 = mcdc.cell(+s33 & -s1 & +s43 & -s44 & +s21 & -s28, fill=m6)
c63 = mcdc.cell(+s1 & -s8 & +s43 & -s11 & +s21 & -s28, fill=m6)
c64 = mcdc.cell(+s1 & -s8 & +s18 & -s44 & +s21 & -s28, fill=m6)
c65 = mcdc.cell(+s8 & -s34 & +s43 & -s44 & +s21 & -s28, fill=m6)
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

