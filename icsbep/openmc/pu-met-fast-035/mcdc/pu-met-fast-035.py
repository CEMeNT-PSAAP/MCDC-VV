import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.03685],
	['Pu240',0.0006736499999999999],
	['Ga69',0.0013940848439999995],
	['Ga71',0.0009252151559999999],
	['C0',0.00030426],
	['Ni58',0.00113688423],
	['Ni60',0.00043792577],
	['Ni61',1.9036329999999998e-05],
	['Ni62',6.069615000000001e-05],
	['Ni64',1.545752e-05]])
# Material Name: Layer 2
# Depletable
m2 = mcdc.material(nuclides=[
	['Pu239',0.036579],
	['Pu240',0.00066875],
	['Ga69',0.00139180074],
	['Ga71',0.00092369926],
	['C0',0.00030205],
	['Ni58',0.0013159264769999999],
	['Ni60',0.000506892523],
	['Ni61',2.2034267e-05],
	['Ni62',7.025488500000001e-05],
	['Ni64',1.7891848000000002e-05]])
# Material Name: Layer 3
# Depletable
m3 = mcdc.material(nuclides=[
	['Pu239',0.036512],
	['Pu240',0.00066739],
	['Ga69',0.0013811616239999998],
	['Ga71',0.000916638376],
	['C0',0.00022608],
	['Ni58',0.0015695810064],
	['Ni60',0.0006045997936],
	['Ni61',2.62815344e-05],
	['Ni62',8.3797032e-05],
	['Ni64',2.1340633599999997e-05]])
# Material Name: Layer 4
# Depletable
m4 = mcdc.material(nuclides=[
	['Pu239',0.036576],
	['Pu240',0.00066878],
	['Ga69',0.001399674888],
	['Ga71',0.000928925112],
	['C0',0.00030206],
	['Ni58',0.0012683407238999998],
	['Ni60',0.0004885625761],
	['Ni61',2.1237476899999993e-05],
	['Ni62',6.77143695e-05],
	['Ni64',1.72448536e-05]])
# Material Name: Layer 5
# Depletable
m5 = mcdc.material(nuclides=[
	['Pu239',0.036471],
	['Pu240',0.0006666499999999999],
	['Ga69',0.0013718448839999998],
	['Ga71',0.0009104551160000001],
	['C0',0.0003011],
	['Ni58',0.0013421360835],
	['Ni60',0.0005169884165],
	['Ni61',2.24731285e-05],
	['Ni62',7.165416750000001e-05],
	['Ni64',1.8248204000000004e-05]])
# Material Name: Lead reflector
m6 = mcdc.material(nuclides=[
	['Pb204',0.00045841600000000006],
	['Pb206',0.007891304],
	['Pb207',0.007236424000000001],
	['Pb208',0.017157856000000003],
	['Fe54',1.07238215e-06],
	['Fe56',1.683410638e-05],
	['Fe57',3.8877293e-07],
	['Fe58',5.1738539999999997e-08]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.2, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.15, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.02, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
c3 = mcdc.cell(+s2 & -s3, fill=m2)
c4 = mcdc.cell(+s3 & -s4, fill=m3)
c5 = mcdc.cell(+s4 & -s5, fill=m4)
c6 = mcdc.cell(+s5 & -s6, fill=m5)
c7 = mcdc.cell(+s6 & -s7, fill=m6)
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

