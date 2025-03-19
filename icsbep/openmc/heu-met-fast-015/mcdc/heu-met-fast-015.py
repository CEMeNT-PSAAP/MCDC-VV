import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Bottom HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.045774],
	['U238',0.0013381],
	['C0',0.0001027],
	['Fe54',2.9342484500000004e-06],
	['Fe56',4.6061425540000005e-05],
	['Fe57',1.06375919e-06],
	['Fe58',1.4156682000000002e-07],
	['W180',1.46388e-09],
	['W182',3.232735e-07],
	['W183',1.7456769e-07],
	['W184',3.7377736e-07],
	['W186',3.4681757e-07]])
# Material Name: Top HEU
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.045708],
	['U238',0.0013404],
	['C0',0.00010256],
	['Fe54',2.93015695e-06],
	['Fe56',4.599719774e-05],
	['Fe57',1.06227589e-06],
	['Fe58',1.4136942e-07],
	['W180',1.46196e-09],
	['W182',3.2284950000000005e-07],
	['W183',1.7433873e-07],
	['W184',3.7328712e-07],
	['W186',3.4636269e-07]])
# Material Name: Steel Diaphragm and Steel Plate
m3 = mcdc.material(nuclides=[
	['Fe54',0.00474222385],
	['Fe56',0.07444277282],
	['Fe57',0.00171920827],
	['Fe58',0.00022879505999999998]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=0.0, bc='vacuum')
s2 = mcdc.surface('plane-z', z=0.21, bc='interface')
s3 = mcdc.surface('plane-z', z=5.17, bc='interface')
s4 = mcdc.surface('plane-z', z=6.17, bc='interface')
s5 = mcdc.surface('plane-z', z=6.22, bc='interface')
s6 = mcdc.surface('plane-z', z=6.43, bc='interface')
s7 = mcdc.surface('plane-z', z=11.39, bc='vacuum')
s8 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=13.0, bc='vacuum')
s9 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=9.995, bc='interface')
s10 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=9.8, bc='interface')
s11 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.75, bc='interface')
s12 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.6, bc='interface')

# Material Cell(s)
c1 = mcdc.cell(+s5 & -s6 & -s8 & +s9, fill=m3)
c2 = mcdc.cell(+s1 & -s2 & -s10, fill=m3)
c3 = mcdc.cell(+s2 & -s4 & -s9 & +s12, fill=m1)
c4 = mcdc.cell(+s2 & -s3 & -s12, fill=m1)
c5 = mcdc.cell(+s5 & -s7 & -s9 & +s11, fill=m2)
c6 = mcdc.cell(+s1 & -s5 & -s8 & +s9, fill=mvoid)
c7 = mcdc.cell(+s6 & -s7 & -s8 & +s9, fill=mvoid)
c8 = mcdc.cell(+s1 & -s2 & -s9 & +s10, fill=mvoid)
c9 = mcdc.cell(+s4 & -s5 & -s9, fill=mvoid)
c10 = mcdc.cell(+s3 & -s4 & -s12, fill=mvoid)
c11 = mcdc.cell(+s5 & -s7 & -s11, fill=mvoid)
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

