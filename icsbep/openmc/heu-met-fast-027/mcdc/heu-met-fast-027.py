import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU, Layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.041828],
	['U238',0.0042699],
	['C0',0.0007319],
	['Fe54',6.9006070000000005e-06],
	['Fe56',0.00010832477240000001],
	['Fe57',2.5016914000000003e-06],
	['Fe58',3.329292e-07],
	['W180',4.30344e-08],
	['W182',9.503430000000002e-06],
	['W183',5.131852200000001e-06],
	['W184',1.09881168e-05],
	['W186',1.0195566600000001e-05]])
# Material Name: HEU, Layer 2
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.041658],
	['U238',0.0041803],
	['C0',0.0014583],
	['Fe54',1.3749193500000001e-05],
	['Fe56',0.00021583293420000002],
	['Fe57',4.9845237e-06],
	['Fe58',6.633486000000001e-07],
	['W180',8.574599999999999e-08],
	['W182',1.8935575e-05],
	['W183',1.02252105e-05],
	['W184',2.1893812e-05],
	['W186',2.0314656499999998e-05]])
# Material Name: HEU, Layer 3
# Depletable
m3 = mcdc.material(nuclides=[
	['U235',0.041312],
	['U238',0.0044603],
	['C0',0.0012746],
	['Fe54',1.2588961e-05],
	['Fe56',0.0001976197652],
	['Fe57',4.5639022e-06],
	['Fe58',6.073716e-07],
	['W180',7.13724e-08],
	['W182',1.5761405e-05],
	['W183',8.5111587e-06],
	['W184',1.82237528e-05],
	['W186',1.69093111e-05]])
# Material Name: HEU, Layer 4
# Depletable
m4 = mcdc.material(nuclides=[
	['U235',0.041823],
	['U238',0.0045031],
	['C0',0.0011052],
	['Fe54',1.15783605e-05],
	['Fe56',0.0001817554986],
	['Fe57',4.1975271e-06],
	['Fe58',5.586138e-07],
	['W180',6.498479999999999e-08],
	['W182',1.4350810000000002e-05],
	['W183',7.7494374e-06],
	['W184',1.65927856e-05],
	['W186',1.53959822e-05]])
# Material Name: HEU, Layer 5
# Depletable
m5 = mcdc.material(nuclides=[
	['U235',0.041769],
	['U238',0.0045313],
	['C0',0.0012895],
	['Fe54',1.2736839500000001e-05],
	['Fe56',0.0001999411414],
	['Fe57',4.6175129e-06],
	['Fe58',6.145062e-07],
	['W180',7.943159999999998e-08],
	['W182',1.7541145e-05],
	['W183',9.4722183e-06],
	['W184',2.0281535199999998e-05],
	['W186',1.88186699e-05]])
# Material Name: HEU, Layer 6
# Depletable
m6 = mcdc.material(nuclides=[
	['U235',0.04239],
	['U238',0.0043476],
	['C0',0.0010214],
	['Fe54',1.05052185e-05],
	['Fe56',0.0001649094642],
	['Fe57',3.8084787e-06],
	['Fe58',5.068386e-07],
	['W180',6.5514e-08],
	['W182',1.4467675e-05],
	['W183',7.8125445e-06],
	['W184',1.6727908e-05],
	['W186',1.55213585e-05]])
# Material Name: HEU, Layer 7
# Depletable
m7 = mcdc.material(nuclides=[
	['U235',0.04236],
	['U238',0.0043676],
	['C0',0.0012074],
	['Fe54',1.2843218500000002e-05],
	['Fe56',0.00020161106419999998],
	['Fe57',4.6560787000000004e-06],
	['Fe58',6.196386e-07],
	['W180',7.28148e-08],
	['W182',1.6079935e-05],
	['W183',8.6831649e-06],
	['W184',1.85920456e-05],
	['W186',1.72510397e-05]])
# Material Name: HEU, Layer 8
# Depletable
m8 = mcdc.material(nuclides=[
	['U235',0.042363],
	['U238',0.0043006],
	['C0',0.00083383],
	['Fe54',9.3175145e-06],
	['Fe56',0.0001462650514],
	['Fe57',3.3778979e-06],
	['Fe58',4.4953619999999997e-07],
	['W180',5.0842799999999997e-08],
	['W182',1.1227785e-05],
	['W183',6.0630038999999996e-06],
	['W184',1.2981861600000001e-05],
	['W186',1.20455067e-05]])
# Material Name: HEU, Layer 9
# Depletable
m9 = mcdc.material(nuclides=[
	['U235',0.042309],
	['U238',0.0043843],
	['C0',0.0009273600000000001],
	['Fe54',9.326282e-06],
	['Fe56',0.0001464026824],
	['Fe57',3.3810764000000005e-06],
	['Fe58',4.4995919999999994e-07],
	['W180',5.08908e-08],
	['W182',1.1238385000000001e-05],
	['W183',6.0687279e-06],
	['W184',1.29941176e-05],
	['W186',1.20568787e-05]])
# Material Name: Lead
m10 = mcdc.material(nuclides=[
	['Pb204',0.000459732],
	['Pb206',0.007913957999999999],
	['Pb207',0.007257198],
	['Pb208',0.017207112],
	['Fe54',1.0754215500000001e-06],
	['Fe56',1.6881818460000003e-05],
	['Fe57',3.8987481e-07],
	['Fe58',5.188518e-08]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.019, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.4, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.15, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.02, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.75, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s10 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s11 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.6, bc='vacuum')

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
c10 = mcdc.cell(+s9 & -s10, fill=m9)
c11 = mcdc.cell(+s10 & -s11, fill=m10)
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

