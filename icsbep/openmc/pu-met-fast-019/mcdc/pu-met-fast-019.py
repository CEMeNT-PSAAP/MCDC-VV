import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.03393],
	['Pu240',0.0035043],
	['Ga69',0.0013286873399999998],
	['Ga71',0.0008818126599999998],
	['C0',0.0030246],
	['Fe54',1.9010862500000002e-05],
	['Fe56',0.000298429885],
	['Fe57',6.8920475e-06],
	['Fe58',9.172050000000001e-07],
	['W180',8.891999999999999e-08],
	['W182',1.96365e-05],
	['W183',1.060371e-05],
	['W184',2.270424e-05],
	['W186',2.1066629999999998e-05],
	['Ni58',0.0009658069803],
	['Ni60',0.00037202711969999995],
	['Ni61',1.6171761299999998e-05],
	['Ni62',5.1562651500000004e-05],
	['Ni64',1.31314872e-05]])
# Material Name: Reflector
# S(a,b): c_Be (Not Implemented)
m2 = mcdc.material(nuclides=[
	['Be9',0.12081],
	['O16',8.2032897744e-05],
	['O17',3.1102256000000005e-08],
	['C0',0.0001002],
	['Fe54',2.97738455e-06],
	['Fe56',4.6738570060000004e-05],
	['Fe57',1.0793974100000001e-06],
	['Fe58',1.4364798e-07]])
# Material Name: Steel
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
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.4, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 1.05], radius=5.35, bc='interface')
s5 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=5.5, bc='interface')
s6 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.1, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.0, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 1.05], radius=11.0, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.15, bc='interface')
s10 = mcdc.surface('plane-z', z=0.0, bc='interface')
s11 = mcdc.surface('plane-z', z=1.0, bc='interface')
s12 = mcdc.surface('plane-z', z=1.2, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=9.7, bc='interface')
s14 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.5, bc='interface')
s15 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=14.0, bc='vacuum')
s16 = mcdc.surface('plane-z', z=-0.15, bc='interface')
s17 = mcdc.surface('plane-z', z=-14.15, bc='vacuum')
s18 = mcdc.surface('plane-z', z=14.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s3, fill=m1)
c3 = mcdc.cell(+s3 & -s4 & +s12, fill=mvoid)
c4 = mcdc.cell(+s3 & -s5 & +s11 & -s12, fill=mvoid)
c5 = mcdc.cell(+s3 & -s7 & -s16, fill=m2)
c6 = mcdc.cell(+s4 & +s6 & -s8 & +s12, fill=m2)
c7 = mcdc.cell(+s3 & +s10 & -s11 & -s15, fill=mvoid)
c8 = mcdc.cell(+s5 & +s11 & -s12 & -s15, fill=m3)
c9 = mcdc.cell(+s7 & -s10 & +s13 & -s15 & +s17, fill=mvoid)
c10 = mcdc.cell(+s8 & +s12 & -s15 & -s18, fill=mvoid)
c11 = mcdc.cell(+s7 & -s9 & -s13 & -s10, fill=m4)
c12 = mcdc.cell(+s9 & -s10 & -s14 & +s17, fill=m3)
c13 = mcdc.cell(+s9 & -s10 & -s13 & +s14 & +s17, fill=mvoid)
c14 = mcdc.cell(+s3 & -s7 & -s10 & +s16, fill=mvoid)
c15 = mcdc.cell(+s4 & -s6 & -s8 & +s12, fill=mvoid)
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
mcdc.source(x=[-0.6,0.6], y=[-0.6,0.6], z=[5.17,6.17], prob=1.0)

mcdc.run()

