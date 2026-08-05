import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU, Layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.041845],
	['U238',0.0045054],
	['C12',0.0011058],
	['Fe54',1.15842055e-05],
	['Fe56',0.0001818472526],
	['Fe57',4.1996461e-06],
	['Fe58',5.588958e-07],
	['W180',6.501959999999999e-08],
	['W182',1.4358495000000001e-05],
	['W183',7.7535873e-06],
	['W184',1.66016712e-05],
	['W186',1.54042269e-05]])
# Material Name: HEU, Layer 2
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.041769],
	['U238',0.0045313],
	['C12',0.0012895],
	['Fe54',1.2736839500000001e-05],
	['Fe56',0.0001999411414],
	['Fe57',4.6175129e-06],
	['Fe58',6.145062e-07],
	['W180',7.943159999999998e-08],
	['W182',1.7541145e-05],
	['W183',9.4722183e-06],
	['W184',2.0281535199999998e-05],
	['W186',1.88186699e-05]])
# Material Name: HEU, Layer 3
# Depletable
m3 = mcdc.material(nuclides=[
	['U235',0.04239],
	['U238',0.0043476],
	['C12',0.0010214],
	['Fe54',1.05052185e-05],
	['Fe56',0.0001649094642],
	['Fe57',3.8084787e-06],
	['Fe58',5.068386e-07],
	['W180',6.5514e-08],
	['W182',1.4467675e-05],
	['W183',7.8125445e-06],
	['W184',1.6727908e-05],
	['W186',1.55213585e-05]])
# Material Name: HEU, Layer 4
# Depletable
m4 = mcdc.material(nuclides=[
	['U235',0.04236],
	['U238',0.0043676],
	['C12',0.0012074],
	['Fe54',1.2843218500000002e-05],
	['Fe56',0.00020161106419999998],
	['Fe57',4.6560787000000004e-06],
	['Fe58',6.196386e-07],
	['W180',7.28148e-08],
	['W182',1.6079935e-05],
	['W183',8.6831649e-06],
	['W184',1.85920456e-05],
	['W186',1.72510397e-05]])
# Material Name: HEU, Layer 5
# Depletable
m5 = mcdc.material(nuclides=[
	['U235',0.042363],
	['U238',0.0043006],
	['C12',0.00083383],
	['Fe54',9.3175145e-06],
	['Fe56',0.0001462650514],
	['Fe57',3.3778979e-06],
	['Fe58',4.4953619999999997e-07],
	['W180',5.0842799999999997e-08],
	['W182',1.1227785e-05],
	['W183',6.0630038999999996e-06],
	['W184',1.2981861600000001e-05],
	['W186',1.20455067e-05]])
# Material Name: HEU, Layer 6
# Depletable
m6 = mcdc.material(nuclides=[
	['U235',0.042309],
	['U238',0.0043843],
	['C12',0.0009273600000000001],
	['Fe54',9.326282e-06],
	['Fe56',0.0001464026824],
	['Fe57',3.3810764000000005e-06],
	['Fe58',4.4995919999999994e-07],
	['W180',5.08908e-08],
	['W182',1.1238385000000001e-05],
	['W183',6.0687279e-06],
	['W184',1.29941176e-05],
	['W186',1.20568787e-05]])
# Material Name: HEU, Layer 7
# Depletable
m7 = mcdc.material(nuclides=[
	['U235',0.042337],
	['U238',0.0043869],
	['C12',0.0013005],
	['Fe54',1.2844972e-05],
	['Fe56',0.0002016385904],
	['Fe57',4.6567144e-06],
	['Fe58',6.197232e-07],
	['W180',7.28232e-08],
	['W182',1.6081790000000002e-05],
	['W183',8.6841666e-06],
	['W184',1.85941904e-05],
	['W186',1.72530298e-05]])
# Material Name: c_Graphite
# S(a,b): c_Graphite (Not Implemented)
m8 = mcdc.material(nuclides=[
	['C12',0.076716]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.029, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.75, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=12.6, bc='vacuum')

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
# Space Type: point
mcdc.source(point=[0.0,0.0,0.0], prob=1.0)

mcdc.run()

