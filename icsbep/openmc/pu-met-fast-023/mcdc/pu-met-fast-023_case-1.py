import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: 98% Pu-239 in delta phase, layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.036825],
	['Pu240',0.00067318],
	['Ga69',0.0013223158919999998],
	['Ga71',0.0008775841079999999],
	['Fe54',8.599748500000001e-06],
	['Fe56',0.0001349976602],
	['Fe57',3.1176847000000002e-06],
	['Fe58',4.149066000000001e-07],
	['C0',0.00030405],
	['Ni58',0.0010703050217999999],
	['Ni60',0.00041227957819999996],
	['Ni61',1.79215078e-05],
	['Ni62',5.7141609e-05],
	['Ni64',1.45522832e-05]])
# Material Name: 98% Pu-239 in delta phase, layer 2
# Depletable
m2 = mcdc.material(nuclides=[
	['Pu239',0.036579],
	['Pu240',0.00066875],
	['Ga69',0.0013292283119999998],
	['Ga71',0.000882171688],
	['Fe54',7.593824000000001e-06],
	['Fe56',0.0001192067968],
	['Fe57',2.7530048e-06],
	['Fe58',3.6637440000000004e-07],
	['C0',0.00030205],
	['Ni58',0.0013159264769999996],
	['Ni60',0.000506892523],
	['Ni61',2.2034267e-05],
	['Ni62',7.025488500000001e-05],
	['Ni64',1.7891848000000002e-05]])
# Material Name: 98% Pu-239 in delta phase, layer 3
# Depletable
m3 = mcdc.material(nuclides=[
	['Pu239',0.036512],
	['Pu240',0.00066739],
	['Ga69',0.00131876952],
	['Ga71',0.0008752304800000001],
	['Fe54',7.5786269999999994e-06],
	['Fe56',0.0001189682364],
	['Fe57',2.7474954000000006e-06],
	['Fe58',3.6564120000000005e-07],
	['C0',0.00022608],
	['Ni58',0.0015695810064],
	['Ni60',0.0006045997936],
	['Ni61',2.62815344e-05],
	['Ni62',8.3797032e-05],
	['Ni64',2.13406336e-05]])
# Material Name: 98% Pu-239 in delta phase, layer 4
# Depletable
m4 = mcdc.material(nuclides=[
	['Pu239',0.036576],
	['Pu240',0.00066878],
	['Ga69',0.0013292884199999997],
	['Ga71',0.00088221158],
	['Fe54',8.5436365e-06],
	['Fe56',0.0001341168218],
	['Fe57',3.0973423e-06],
	['Fe58',4.121994e-07],
	['C0',0.00030206],
	['Ni58',0.0012683407238999998],
	['Ni60',0.0004885625761],
	['Ni61',2.1237476899999997e-05],
	['Ni62',6.77143695e-05],
	['Ni64',1.72448536e-05]])
# Material Name: 98% Pu-239 in delta phase, layer 5
# Depletable
m5 = mcdc.material(nuclides=[
	['Pu239',0.036471],
	['Pu240',0.0006666500000000001],
	['Ga69',0.001301698848],
	['Ga71',0.0008639011520000001],
	['Fe54',8.516749500000001e-06],
	['Fe56',0.0001336947534],
	['Fe57',3.0875949000000004e-06],
	['Fe58',4.1090220000000005e-07],
	['C0',0.0003011],
	['Ni58',0.0013421360835],
	['Ni60',0.0005169884165],
	['Ni61',2.24731285e-05],
	['Ni62',7.165416750000001e-05],
	['Ni64',1.8248204000000004e-05]])
# Material Name: c_Graphite
# S(a,b): c_Graphite (Not Implemented)
m6 = mcdc.material(nuclides=[
	['C0',0.091842]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.715, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.15, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.02, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='vacuum')

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

