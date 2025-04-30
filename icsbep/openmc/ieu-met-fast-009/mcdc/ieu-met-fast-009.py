import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: 36 wt% U-235, Layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.01744],
	['U238',0.02999],
	['C0',0.00047009],
	['Fe54',9.454872e-06],
	['Fe56',0.0001484212704],
	['Fe57',3.4276943999999994e-06],
	['Fe58',4.561632e-07],
	['W180',1.4740799999999999e-08],
	['W182',3.25526e-06],
	['W183',1.7578404000000002e-06],
	['W184',3.7638175999999998e-06],
	['W186',3.4923412e-06]])
# Material Name: 36 wt% U-235, Layer 2
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.017415],
	['U238',0.029887],
	['C0',0.00037502],
	['Fe54',9.428569500000001e-06],
	['Fe56',0.00014800837740000001],
	['Fe57',3.4181589000000006e-06],
	['Fe58',4.548942e-07],
	['W180',1.4699999999999998e-08],
	['W182',3.24625e-06],
	['W183',1.752975e-06],
	['W184',3.7534e-06],
	['W186',3.4826749999999992e-06]])
# Material Name: 36 wt% U-235, Layer 3
# Depletable
m3 = mcdc.material(nuclides=[
	['U235',0.017418],
	['U238',0.029651],
	['C0',0.00055986],
	['Fe54',9.383563e-06],
	['Fe56',0.0001473018716],
	['Fe57',3.4018426e-06],
	['Fe58',4.527228e-07],
	['W180',1.4630399999999996e-08],
	['W182',3.2308799999999997e-06],
	['W183',1.7446752e-06],
	['W184',3.7356287999999997e-06],
	['W186',3.4661856000000002e-06]])
# Material Name: 36 wt% U-235, Layer 4
# Depletable
m4 = mcdc.material(nuclides=[
	['U235',0.017356],
	['U238',0.029786],
	['C0',0.00074727],
	['Fe54',7.045562999999999e-06],
	['Fe56',0.0001106002716],
	['Fe57',2.5542426e-06],
	['Fe58',3.399228e-07],
	['W180',1.4645999999999998e-08],
	['W182',3.234325e-06],
	['W183',1.7465355000000002e-06],
	['W184',3.7396119999999996e-06],
	['W186',3.4698815000000002e-06]])
# Material Name: 36 wt% U-235, Layer 5
# Depletable
m5 = mcdc.material(nuclides=[
	['U235',0.017417],
	['U238',0.029662999999999995],
	['C0',0.00055983],
	['Fe54',5.864873000000001e-06],
	['Fe56',9.206596360000001e-05],
	['Fe57',2.1262046000000002e-06],
	['Fe58',2.8295880000000003e-07],
	['W180',7.31472e-09],
	['W182',1.6153340000000003e-06],
	['W183',8.7228036e-07],
	['W184',1.86769184e-06],
	['W186',1.7329790799999999e-06]])
# Material Name: Polyethylene, Layer 1
# S(a,b): c_H_in_CH2 (Not Implemented)
m6 = mcdc.material(nuclides=[
	['H1',0.075542],
	['C0',0.037771]])
# Material Name: Polyethylene, Layer 2
# S(a,b): c_H_in_CH2 (Not Implemented)
m7 = mcdc.material(nuclides=[
	['H1',0.07417],
	['C0',0.037085]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.445, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.0, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=12.25, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=15.15, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=18.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
c3 = mcdc.cell(+s2 & -s3, fill=m2)
c4 = mcdc.cell(+s3 & -s4, fill=m3)
c5 = mcdc.cell(+s4 & -s5, fill=m4)
c6 = mcdc.cell(+s5 & -s6, fill=m5)
c7 = mcdc.cell(+s6 & -s7, fill=m6)
c8 = mcdc.cell(+s7 & -s8, fill=m7)
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

