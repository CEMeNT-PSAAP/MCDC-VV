import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Aluminum
m1 = mcdc.material(nuclides=[
	['Al27',0.060239]])
# Material Name: Depleted Uranium
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',9.736e-05],
	['U238',0.047969]])
# Material Name: SAE 1020 Steel
m3 = mcdc.material(nuclides=[
	['Fe54',0.00404865615],
	['Fe56',0.06355524318],
	['Fe57',0.00146776773],
	['Fe58',0.00019533293999999998],
	['C0',0.00054977],
	['Mn55',0.00016969]])
# Material Name: Fe
m4 = mcdc.material(nuclides=[
	['Fe54',0.0050169973],
	['Fe56',0.07875612836],
	['Fe57',0.00181882246],
	['Fe58',0.00024205187999999997]])
# Material Name: Be
# S(a,b): c_Be (Not Implemented)
m5 = mcdc.material(nuclides=[
	['Be9',0.12295]])
# Material Name: HEU, Can I
# Depletable
m11 = mcdc.material(nuclides=[
	['U235',0.02345],
	['U238',0.0013421],
	['H1',0.07385949533046],
	['H2',1.1504669540000001e-05],
	['O16',0.00085520575413],
	['O17',3.2424587e-07],
	['C0',0.00014562],
	['N14',0.0013543208841],
	['N15',4.9791159e-06],
	['Fe54',2.14377065e-06],
	['Fe56',3.3652614580000005e-05],
	['Fe57',7.7718563e-07],
	['Fe58',1.0342914000000001e-07],
	['Au197',0.0003398]])
# Material Name: HEU, Can II
# Depletable
m12 = mcdc.material(nuclides=[
	['U235',0.023409],
	['U238',0.0013371],
	['H1',0.07538425782696001],
	['H2',1.174217304e-05],
	['O16',0.00056681509563],
	['O17',2.1490437000000002e-07],
	['C0',0.00019893],
	['N14',0.00019626842563],
	['N15',7.2157437e-07],
	['Fe54',2.2366477e-06],
	['Fe56',3.5110585640000004e-05],
	['Fe57',8.108565399999999e-07],
	['Fe58',1.0791012000000002e-07],
	['Au197',0.00033787]])
# Material Name: HEU, Can III
# Depletable
m13 = mcdc.material(nuclides=[
	['U235',0.02355],
	['U238',0.0013584],
	['H1',0.06990211174938],
	['H2',1.088825062e-05],
	['O16',0.00048405647303999993],
	['O17',1.8352696e-07],
	['C0',0.00015288],
	['N14',0.00020568381028],
	['N15',7.5618972e-07],
	['Fe54',6.058926999999999e-06],
	['Fe56',9.511219639999999e-05],
	['Fe57',2.1965554e-06],
	['Fe58',2.9232119999999997e-07],
	['Au197',0.00034242]])
# Material Name: HEU, Can IV
# Depletable
m14 = mcdc.material(nuclides=[
	['U235',0.022939],
	['U238',0.0013117],
	['H1',0.0727136738085],
	['H2',1.13261915e-05],
	['O16',0.00063688852773],
	['O17',2.4147227e-07],
	['C0',0.00015539],
	['N14',0.00024310622800000002],
	['N15',8.93772e-07],
	['Fe54',1.19442575e-06],
	['Fe56',1.8749929900000002e-05],
	['Fe57',4.3301765e-07],
	['Fe58',5.76267e-08],
	['Au197',0.00034196]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=-1.27, bc='vacuum')
s2 = mcdc.surface('plane-z', z=0.0, bc='interface')
s3 = mcdc.surface('plane-z', z=2.34, bc='interface')
s4 = mcdc.surface('plane-z', z=2.4988, bc='interface')
s5 = mcdc.surface('plane-z', z=2.5242, bc='interface')
s6 = mcdc.surface('plane-z', z=5.5248, bc='interface')
s7 = mcdc.surface('plane-z', z=5.5502, bc='interface')
s8 = mcdc.surface('plane-z', z=5.5756, bc='interface')
s9 = mcdc.surface('plane-z', z=8.5849, bc='interface')
s10 = mcdc.surface('plane-z', z=8.6103, bc='interface')
s11 = mcdc.surface('plane-z', z=9.5509, bc='interface')
s12 = mcdc.surface('plane-z', z=9.5763, bc='interface')
s13 = mcdc.surface('plane-z', z=12.5719, bc='interface')
s14 = mcdc.surface('plane-z', z=12.5973, bc='interface')
s15 = mcdc.surface('plane-z', z=12.6227, bc='interface')
s16 = mcdc.surface('plane-z', z=15.5948, bc='interface')
s17 = mcdc.surface('plane-z', z=15.6202, bc='interface')
s18 = mcdc.surface('plane-z', z=15.779, bc='interface')
s19 = mcdc.surface('plane-z', z=18.119, bc='interface')
s20 = mcdc.surface('plane-z', z=19.9085, bc='vacuum')
s21 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=6.0325, bc='interface')
s22 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=6.35, bc='interface')
s23 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=7.505, bc='interface')
s24 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=7.5438, bc='interface')
s25 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=7.5489, bc='interface')
s26 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=7.6759, bc='interface')
s27 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=7.7013, bc='interface')
s28 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=10.0432, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s2 & -s28, fill=m1)
c2 = mcdc.cell(+s2 & -s3 & -s24, fill=m5)
c3 = mcdc.cell(+s3 & -s4 & -s23, fill=m3)
c4 = mcdc.cell(+s3 & -s4 & +s23 & -s24, fill=mvoid)
c5 = mcdc.cell(+s4 & -s5 & -s24, fill=m3)
c6 = mcdc.cell(+s5 & -s6 & -s23, fill=m11)
c7 = mcdc.cell(+s5 & -s6 & +s23 & -s24, fill=m3)
c8 = mcdc.cell(+s6 & -s7 & -s24, fill=m3)
c9 = mcdc.cell(+s7 & -s8 & -s24, fill=m3)
c10 = mcdc.cell(+s8 & -s9 & -s23, fill=m14)
c11 = mcdc.cell(+s8 & -s9 & +s23 & -s24, fill=m3)
c12 = mcdc.cell(+s9 & -s10 & -s24, fill=m3)
c13 = mcdc.cell(+s10 & -s11 & -s21, fill=mvoid)
c14 = mcdc.cell(+s10 & -s11 & +s21 & -s22, fill=m1)
c15 = mcdc.cell(+s10 & -s11 & +s22 & -s24, fill=mvoid)
c16 = mcdc.cell(+s11 & -s12 & -s24, fill=m3)
c17 = mcdc.cell(+s12 & -s13 & -s23, fill=m13)
c18 = mcdc.cell(+s12 & -s13 & +s23 & -s24, fill=m3)
c19 = mcdc.cell(+s13 & -s14 & -s24, fill=m3)
c20 = mcdc.cell(+s14 & -s15 & -s24, fill=m3)
c21 = mcdc.cell(+s15 & -s16 & -s23, fill=m12)
c22 = mcdc.cell(+s15 & -s16 & +s23 & -s24, fill=m3)
c23 = mcdc.cell(+s16 & -s17 & -s24, fill=m3)
c24 = mcdc.cell(+s17 & -s18 & -s23, fill=m3)
c25 = mcdc.cell(+s17 & -s18 & +s23 & -s24, fill=mvoid)
c26 = mcdc.cell(+s18 & -s19 & -s24, fill=m5)
c27 = mcdc.cell(+s19 & -s20 & -s24, fill=mvoid)
c28 = mcdc.cell(+s2 & -s20 & +s24 & -s25, fill=mvoid)
c29 = mcdc.cell(+s2 & -s20 & +s25 & -s26, fill=m4)
c30 = mcdc.cell(+s2 & -s20 & +s26 & -s27, fill=mvoid)
c31 = mcdc.cell(+s2 & -s20 & +s27 & -s28, fill=m5)
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
mcdc.source(x=[-1.0,1.0], y=[-1.0,1.0], z=[9.8803,10.4322], prob=1.0)

mcdc.run()

