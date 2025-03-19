import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Enriched U metal (37.5 w/o)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.01773],
	['U238',0.028957],
	['C0',0.00018452],
	['O16',0.00034617874851],
	['O17',1.3125149e-07],
	['Fe54',3.47935315e-06],
	['Fe56',5.4618403580000004e-05],
	['Fe57',1.26137713e-06],
	['Fe58',1.6786614e-07],
	['Al27',4.107e-05],
	['H1',4.397115086628e-05],
	['H2',6.84913372e-09],
	['Si28',3.639014254080001e-05],
	['Si29',1.8477876096000002e-06],
	['Si30',1.2180698496e-06]])
# Material Name: Natural U metal
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.00033316],
	['U238',0.045948],
	['C0',0.00049205],
	['Fe54',6.1857635e-06],
	['Fe56',9.71032582e-05],
	['Fe57',2.2425377e-06],
	['Fe58',2.9844059999999997e-07],
	['H1',4.397115086628e-05],
	['H2',6.84913372e-09],
	['Si28',0.00019407891562400005],
	['Si29',9.854773588e-06],
	['Si30',6.496310788e-06]])
# Material Name: Sheath
m3 = mcdc.material(nuclides=[
	['C0',0.00077829],
	['Fe54',0.0033096728000000003],
	['Fe56',0.05195478496],
	['Fe57',0.00119986256],
	['Fe58',0.00015967968],
	['Cr50',0.0006998491500000002],
	['Cr52',0.01349589423],
	['Cr53',0.00153032607],
	['Cr54',0.00038093055],
	['Cu63',5.10693495e-05],
	['Cu65',2.2783650499999998e-05],
	['Mo100',1.4260344e-05],
	['Mo92',2.1438811500000004e-05],
	['Mo94',1.34451745e-05],
	['Mo95',2.3230135500000004e-05],
	['Mo96',2.44009355e-05],
	['Mo97',1.4023257e-05],
	['Mo98',3.5551342e-05],
	['Mn55',0.0011918],
	['Ni58',0.006129712152899999],
	['Ni60',0.0023611541470999996],
	['Ni61',0.0001026377359],
	['Ni62',0.0003272540145],
	['Ni64',8.334194959999999e-05],
	['Al27',0.00034646],
	['Ti46',2.419395e-05],
	['Ti47',2.1818543999999998e-05],
	['Ti48',0.000216191272],
	['Ti49',1.5865366e-05],
	['Ti50',1.5190867999999998e-05],
	['H1',2.271046252164e-05],
	['H2',3.53747836e-09],
	['Si28',0.0009221861243840001],
	['Si29',4.682598020800001e-05],
	['Si30',3.0867895408e-05],
	['V50',2.303175e-07],
	['V51',9.18966825e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-x', x=-2.6272, bc='reflective')
s2 = mcdc.surface('plane-x', x=-2.551, bc='interface')
s3 = mcdc.surface('plane-x', x=-2.5335, bc='interface')
s4 = mcdc.surface('plane-x', x=2.5335, bc='interface')
s5 = mcdc.surface('plane-x', x=2.551, bc='interface')
s6 = mcdc.surface('plane-x', x=2.6272, bc='reflective')
s7 = mcdc.surface('plane-y', y=-2.6272, bc='reflective')
s8 = mcdc.surface('plane-y', y=-2.551, bc='interface')
s9 = mcdc.surface('plane-y', y=-2.5335, bc='interface')
s10 = mcdc.surface('plane-y', y=2.5335, bc='interface')
s11 = mcdc.surface('plane-y', y=2.551, bc='interface')
s12 = mcdc.surface('plane-y', y=2.6272, bc='reflective')
s13 = mcdc.surface('plane-z', z=-1.11125, bc='reflective')
s14 = mcdc.surface('plane-z', z=-0.79375, bc='interface')
s15 = mcdc.surface('plane-z', z=-0.47625, bc='interface')
s16 = mcdc.surface('plane-z', z=-0.15875, bc='interface')
s17 = mcdc.surface('plane-z', z=0.15875, bc='interface')
s18 = mcdc.surface('plane-z', z=0.47625, bc='interface')
s19 = mcdc.surface('plane-z', z=0.79375, bc='interface')
s20 = mcdc.surface('plane-z', z=1.11125, bc='reflective')

# Material Cell(s)
c1 = mcdc.cell(+s3 & -s4 & +s9 & -s10 & +s13 & -s14, fill=m2)
c2 = mcdc.cell(+s3 & -s4 & +s9 & -s10 & +s14 & -s15, fill=m2)
c3 = mcdc.cell(+s3 & -s4 & +s9 & -s10 & +s15 & -s16, fill=m2)
c4 = mcdc.cell(+s3 & -s4 & +s9 & -s10 & +s16 & -s17, fill=m1)
c5 = mcdc.cell(+s3 & -s4 & +s9 & -s10 & +s17 & -s18, fill=m2)
c6 = mcdc.cell(+s3 & -s4 & +s9 & -s10 & +s18 & -s19, fill=m2)
c7 = mcdc.cell(+s3 & -s4 & +s9 & -s10 & +s19 & -s20, fill=m2)
c8 = mcdc.cell(+s2 & -s3 & +s8 & -s11 & +s13 & -s20, fill=mvoid)
c9 = mcdc.cell(+s3 & -s4 & +s8 & -s9 & +s13 & -s20, fill=mvoid)
c10 = mcdc.cell(+s4 & -s5 & +s8 & -s11 & +s13 & -s20, fill=mvoid)
c11 = mcdc.cell(+s3 & -s4 & +s10 & -s11 & +s13 & -s20, fill=mvoid)
c12 = mcdc.cell(+s1 & -s2 & +s7 & -s12 & +s13 & -s20, fill=m3)
c13 = mcdc.cell(+s2 & -s5 & +s7 & -s8 & +s13 & -s20, fill=m3)
c14 = mcdc.cell(+s5 & -s6 & +s7 & -s12 & +s13 & -s20, fill=m3)
c15 = mcdc.cell(+s2 & -s5 & +s11 & -s12 & +s13 & -s20, fill=m3)
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
mcdc.source(x=[-2.6272,2.6272], y=[-2.6272,2.6272], z=[-1.11125,1.11125], prob=1.0)

mcdc.run()

