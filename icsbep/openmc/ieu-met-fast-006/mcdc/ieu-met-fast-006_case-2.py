import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: 36 wt% U-235
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.017161],
	['U238',0.02931],
	['W180',1.28652e-08],
	['W182',2.841065e-06],
	['W183',1.5341751000000002e-06],
	['W184',3.2849144e-06],
	['W186',3.0479802999999996e-06],
	['Fe54',7.2156524999999994e-06],
	['Fe56',0.00011327031299999999],
	['Fe57',2.6159055e-06],
	['Fe58',3.48129e-07],
	['C0',0.00064888],
	['Cu63',0.00018501082500000003],
	['Cu65',8.253917500000001e-05],
	['Ni58',0.00019721197160999998],
	['Ni60',7.596569839e-05],
	['Ni61',3.3021763099999997e-06],
	['Ni62',1.0528783050000001e-05],
	['Ni64',2.68137064e-06]])
# Material Name: Duralumin reflector #1
m2 = mcdc.material(nuclides=[
	['Al27',0.052342],
	['Fe54',5.5988085999999995e-05],
	['Fe56',0.0008788932152],
	['Fe57',2.02974772e-05],
	['Fe58',2.7012216e-06],
	['Cu63',0.00068191581],
	['Cu65',0.00030422418999999997]])
# Material Name: Duralumin reflector #2
m3 = mcdc.material(nuclides=[
	['Al27',0.052067],
	['Fe54',5.5694667e-05],
	['Fe56',0.0008742871644000001],
	['Fe57',2.0191103400000002e-05],
	['Fe58',2.6870652e-06],
	['Cu63',0.0006783407550000001],
	['Cu65',0.000302629245]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=2.1, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=13.25, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=15.0, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=25.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
c3 = mcdc.cell(+s2 & -s3, fill=m2)
c4 = mcdc.cell(+s3 & -s4, fill=m3)
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

