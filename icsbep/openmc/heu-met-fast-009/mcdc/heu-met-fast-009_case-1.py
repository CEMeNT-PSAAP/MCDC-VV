import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.041],
	['U238',0.0040977],
	['C0',0.00039932],
	['Fe54',7.9088695e-06],
	['Fe56',0.00012415233740000002],
	['Fe57',2.8672189000000002e-06],
	['Fe58',3.815742e-07],
	['W180',1.4934e-08],
	['W182',3.297925e-06],
	['W183',1.7808795000000001e-06],
	['W184',3.8131480000000004e-06],
	['W186',3.5381135e-06],
	['Cu63',0.00050710461],
	['Cu65',0.00022623539],
	['Ni58',0.00023165888300999998],
	['Ni60',8.923458698999999e-05],
	['Ni61',3.87896571e-06],
	['Ni62',1.236784005e-05],
	['Ni64',3.14972424e-06]])
# Material Name: Be Reflector
# S(a,b): c_Be (Not Implemented)
m2 = mcdc.material(nuclides=[
	['Be9',0.1208],
	['O16',8.202190191299999e-05],
	['O17',3.1098086999999996e-08],
	['C0',0.00010019],
	['Fe54',2.9769754e-06],
	['Fe56',4.673214728e-05],
	['Fe57',1.07924908e-06],
	['Fe58',1.4362824e-07]])
# Material Name: Fe
m3 = mcdc.material(nuclides=[
	['Fe54',0.0047446203],
	['Fe56',0.07448039196],
	['Fe57',0.00172007706],
	['Fe58',0.00022891068]])
# Material Name: Copper
m4 = mcdc.material(nuclides=[
	['Cu63',0.0569553975],
	['Cu65',0.025409602499999996]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=7.75, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 2.06], radius=7.55, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 2.06], radius=8.35, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.0, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 2.06], radius=11.0, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.15, bc='interface')
s9 = mcdc.surface('plane-z', z=0.0, bc='interface')
s10 = mcdc.surface('plane-z', z=1.86, bc='interface')
s11 = mcdc.surface('plane-z', z=2.06, bc='interface')
s12 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=9.7, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.5, bc='interface')
s14 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=14.0, bc='vacuum')
s15 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.1, bc='interface')
s16 = mcdc.surface('cylinder-y', center=[0.0, 0.0], radius=0.6, bc='interface')
s17 = mcdc.surface('cylinder-y', center=[0.0, 2.06], radius=0.6, bc='interface')
s18 = mcdc.surface('plane-z', z=-0.15, bc='interface')
s19 = mcdc.surface('plane-z', z=2.21, bc='interface')
s20 = mcdc.surface('plane-z', z=-14.15, bc='vacuum')
s21 = mcdc.surface('plane-z', z=14.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s16 & -s2, fill=mvoid)
c2 = mcdc.cell(-s15 & +s5 & -s7 & +s11, fill=mvoid)
c3 = mcdc.cell(-s2 & +s16, fill=m1)
c4 = mcdc.cell(+s2 & -s3 & +s11, fill=mvoid)
c5 = mcdc.cell(+s2 & -s4 & -s9 & +s16, fill=m1)
c6 = mcdc.cell(+s3 & -s5 & +s11 & +s17, fill=m1)
c7 = mcdc.cell(+s4 & -s6 & -s18, fill=m2)
c8 = mcdc.cell(+s5 & -s7 & +s19 & +s15, fill=m2)
c9 = mcdc.cell(+s2 & +s9 & -s10 & -s14, fill=mvoid)
c10 = mcdc.cell(+s1 & +s10 & -s11 & -s14, fill=m3)
c11 = mcdc.cell(+s6 & -s14 & -s9 & +s12 & +s20, fill=mvoid)
c12 = mcdc.cell(+s7 & -s14 & +s11 & -s21, fill=mvoid)
c13 = mcdc.cell(+s6 & -s8 & -s12 & -s9, fill=m4)
c14 = mcdc.cell(+s8 & -s14 & -s13 & -s9 & +s20, fill=m3)
c15 = mcdc.cell(+s8 & -s14 & +s13 & -s12 & -s9 & +s20, fill=mvoid)
c16 = mcdc.cell(+s2 & -s1 & +s10 & -s11, fill=mvoid)
c17 = mcdc.cell(+s4 & -s6 & +s18 & -s9, fill=mvoid)
c18 = mcdc.cell(+s5 & -s7 & +s11 & -s19, fill=mvoid)
c19 = mcdc.cell(-s9 & +s2 & -s4 & -s16, fill=mvoid)
c20 = mcdc.cell(+s3 & -s5 & +s11 & -s17, fill=mvoid)
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
mcdc.source(x=[-1.0,1.0], y=[-1.0,1.0], z=[-1.0,1.0], prob=1.0)

mcdc.run()

