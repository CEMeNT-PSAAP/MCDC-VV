import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.036581],
	['Pu240',0.0006687999999999999],
	['Ga69',0.0013916204159999997],
	['Ga71',0.0009235795839999999],
	['C0',0.00030207],
	['Ni58',0.0013078934028],
	['Ni60',0.0005037981972],
	['Ni61',2.1899758799999998e-05],
	['Ni62',6.9826014e-05],
	['Ni64',1.7782627200000002e-05]])
# Material Name: Layer 2
# Depletable
m2 = mcdc.material(nuclides=[
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
# Material Name: Layer 3
# Depletable
m3 = mcdc.material(nuclides=[
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
# Material Name: Layer 4
# Depletable
m4 = mcdc.material(nuclides=[
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
# Material Name: Layer 5
# Depletable
m5 = mcdc.material(nuclides=[
	['Pu239',0.036707],
	['Pu240',0.0006711],
	['Ga69',0.001396669488],
	['Ga71',0.000926930512],
	['C0',0.00030311],
	['Ni58',0.0011221115426999998],
	['Ni60',0.00043223535729999997],
	['Ni61',1.8788971699999998e-05],
	['Ni62',5.99074635e-05],
	['Ni64',1.52566648e-05]])
# Material Name: Duralumin reflector, layer 1
m6 = mcdc.material(nuclides=[
	['Al27',0.055645],
	['Fe54',5.951963500000001e-05],
	['Fe56',0.000934330982],
	['Fe57',2.1577777e-05],
	['Fe58',2.871606e-06],
	['Cu63',0.0007249686],
	['Cu65',0.0003234314]])
# Material Name: Duralumin reflector, layer 2
m7 = mcdc.material(nuclides=[
	['Al27',0.053497],
	['Fe54',5.7223719000000004e-05],
	['Fe56',0.0008982900107999999],
	['Fe57',2.07454338e-05],
	['Fe58',2.7608364e-06],
	['Cu63',0.0006969628499999999],
	['Cu65',0.00031093715]])
# Material Name: Duralumin reflector, layer 3
m8 = mcdc.material(nuclides=[
	['Al27',0.051557],
	['Fe54',5.5149328500000005e-05],
	['Fe56',0.0008657265162000001],
	['Fe57',1.9993400700000002e-05],
	['Fe58',2.6607546e-06],
	['Cu63',0.00067169544],
	['Cu65',0.00029966456]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.112, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.02, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.75, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.0, bc='vacuum')

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

