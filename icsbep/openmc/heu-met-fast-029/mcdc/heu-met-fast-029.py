import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU, Layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.041441],
	['U238',0.0042953],
	['Cu63',0.000511246695],
	['Cu65',0.000228083305],
	['C0',0.00054396],
	['Ni58',0.0003642794919],
	['Ni60',0.0001403198081],
	['Ni61',6.0996049e-06],
	['Ni62',1.9448209500000004e-05],
	['Ni64',4.952885600000001e-06]])
# Material Name: HEU, Layer 2
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.041478],
	['U238',0.004239],
	['Cu63',0.000517345725],
	['Cu65',0.000230804275],
	['C0',0.00054378],
	['Ni58',0.00040539113180999994],
	['Ni60',0.00015615593818999997],
	['Ni61',6.78799051e-06],
	['Ni62',2.1643084049999998e-05],
	['Ni64',5.51185544e-06]])
# Material Name: HEU, Layer 3
# Depletable
m3 = mcdc.material(nuclides=[
	['U235',0.040925],
	['U238',0.0042922],
	['Cu63',0.00064132476],
	['Cu65',0.00028611524],
	['C0',0.00053785],
	['Ni58',0.00045987307487999995],
	['Ni60',0.00017714228512],
	['Ni61',7.70025248e-06],
	['Ni62',2.45517744e-05],
	['Ni64',6.252613119999999e-06]])
# Material Name: HEU, Layer 4
# Depletable
m4 = mcdc.material(nuclides=[
	['U235',0.041135],
	['U238',0.0042744],
	['Cu63',0.00059605917],
	['Cu65',0.00026592083],
	['C0',0.00054074],
	['Ni58',0.00029671316865],
	['Ni60',0.00011429338134999998],
	['Ni61',4.968254149999999e-06],
	['Ni62',1.584096825e-05],
	['Ni64',4.0342276000000004e-06]])
# Material Name: HEU, Layer 5
# Depletable
m5 = mcdc.material(nuclides=[
	['U235',0.041062],
	['U238',0.0042174],
	['Cu63',0.0005793179550000001],
	['Cu65',0.00025845204500000004],
	['C0',0.00044891],
	['Ni58',0.00033665388588],
	['Ni60',0.00012967847412],
	['Ni61',5.63703348e-06],
	['Ni62',1.7973329400000002e-05],
	['Ni64',4.57727712e-06]])
# Material Name: HEU, Layer 6
# Depletable
m6 = mcdc.material(nuclides=[
	['U235',0.041306],
	['U238',0.0042137],
	['Cu63',0.0005561872799999999],
	['Cu65',0.00024813271999999997],
	['C0',0.00036114],
	['Ni58',0.00037831694867999997],
	['Ni60',0.00014572701132],
	['Ni61',6.3346522799999985e-06],
	['Ni62',2.0197643400000002e-05],
	['Ni64',5.14374432e-06]])
# Material Name: HEU, Layer 7
# Depletable
m7 = mcdc.material(nuclides=[
	['U235',0.041191],
	['U238',0.0041791],
	['Cu63',0.00043980783000000006],
	['Cu65',0.00019621217000000005],
	['C0',0.00035973],
	['Ni58',0.00024106030289999998],
	['Ni60',9.285599709999998e-05],
	['Ni61',4.036385899999999e-06],
	['Ni62',1.28697645e-05],
	['Ni64',3.2775496e-06]])
# Material Name: Depleted uranium, Layer 1
# Depletable
m8 = mcdc.material(nuclides=[
	['U235',0.00021044],
	['U238',0.04678],
	['C0',0.0029015],
	['Fe54',2.2354787e-05],
	['Fe56',0.0003509223484],
	['Fe57',8.1043274e-06],
	['Fe58',1.0785372e-06]])
# Material Name: Depleted uranium, Layer 2
# Depletable
m9 = mcdc.material(nuclides=[
	['U235',0.00021047],
	['U238',0.046786],
	['C0',0.0029018],
	['Fe54',2.23577095e-05],
	['Fe56',0.00035096822540000005],
	['Fe57',8.1053869e-06],
	['Fe58',1.0786782e-06]])
# Material Name: Depleted uranium, Layer 3
# Depletable
m10 = mcdc.material(nuclides=[
	['U235',0.00021912],
	['U238',0.045586],
	['C0',0.0028282],
	['Fe54',2.17907445e-05],
	['Fe56',0.0003420680874],
	['Fe57',7.8998439e-06],
	['Fe58',1.0513242000000001e-06]])
# Material Name: Depleted uranium, Layer 4
# Depletable
m11 = mcdc.material(nuclides=[
	['U235',0.00021059],
	['U238',0.045767],
	['C0',0.0028389],
	['Fe54',2.1873159e-05],
	['Fe56',0.0003433618188],
	['Fe57',7.9297218e-06],
	['Fe58',1.0553003999999998e-06]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.91, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.15, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.01, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.75, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s10 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='interface')
s11 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.0, bc='interface')
s12 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=12.25, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
c3 = mcdc.cell(+s2 & -s3, fill=m2)
c4 = mcdc.cell(+s3 & -s4, fill=m3)
c5 = mcdc.cell(+s4 & -s5, fill=m4)
c6 = mcdc.cell(+s5 & -s6, fill=m5)
c7 = mcdc.cell(+s6 & -s7, fill=m6)
c8 = mcdc.cell(+s7 & -s8, fill=m7)
c9 = mcdc.cell(+s8 & -s9, fill=m8)
c10 = mcdc.cell(+s9 & -s10, fill=m9)
c11 = mcdc.cell(+s10 & -s11, fill=m10)
c12 = mcdc.cell(+s11 & -s12, fill=m11)
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

