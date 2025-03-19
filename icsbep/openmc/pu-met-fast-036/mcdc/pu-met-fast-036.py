import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.035932],
	['Pu240',0.00065685],
	['Ga69',0.00135934242],
	['Ga71',0.00090215758],
	['C0',0.00029667],
	['Ni58',0.0028752278714999995],
	['Ni60',0.0011075326285],
	['Ni61',4.814367649999999e-05],
	['Ni62',0.00015350310750000001],
	['Ni64',3.9092716e-05]])
# Material Name: Layer 2
# Depletable
m2 = mcdc.material(nuclides=[
	['Pu239',0.036826],
	['Pu240',0.0006732000000000001],
	['Ga69',0.0013931832239999999],
	['Ga71',0.000924616776],
	['C0',0.00030406],
	['Ni58',0.0010703050217999999],
	['Ni60',0.00041227957819999996],
	['Ni61',1.79215078e-05],
	['Ni62',5.7141609e-05],
	['Ni64',1.4552283199999998e-05]])
# Material Name: Layer 3
# Depletable
m3 = mcdc.material(nuclides=[
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
# Material Name: Layer 4
# Depletable
m4 = mcdc.material(nuclides=[
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
# Material Name: Layer 5
# Depletable
m5 = mcdc.material(nuclides=[
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
# Material Name: Layer 6
# Depletable
m6 = mcdc.material(nuclides=[
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
# Material Name: Cadmium reflector
m7 = mcdc.material(nuclides=[
	['Cd106',0.000576933],
	['Cd108',0.0004114992],
	['Cd110',0.005778598],
	['Cd111',0.005929203],
	['Cd112',0.0111721106],
	['Cd113',0.0056659918],
	['Cd114',0.0133246036],
	['Cd116',0.0034810608]])
# Material Name: Polyethlyene reflector, layer 1
# S(a,b): c_H_in_CH2 (Not Implemented)
m8 = mcdc.material(nuclides=[
	['H1',0.07383349937969999],
	['H2',1.15006203e-05],
	['C0',0.036922]])
# Material Name: Polyethlyene reflector, layer 2
# S(a,b): c_H_in_CH2 (Not Implemented)
m9 = mcdc.material(nuclides=[
	['H1',0.07898469700722],
	['H2',1.2302992779999999e-05],
	['C0',0.039498]])
# Material Name: Polyethlyene reflector, layer 3
# S(a,b): c_H_in_CH2 (Not Implemented)
m10 = mcdc.material(nuclides=[
	['H1',0.07898369716296],
	['H2',1.2302837039999999e-05],
	['C0',0.039498]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.16, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.4, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.15, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.02, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.05, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.75, bc='interface')
s10 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s11 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='vacuum')

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
# Space Type: box
mcdc.source(x=[-1.0,1.0], y=[-1.0,1.0], z=[-1.0,1.0], prob=1.0)

mcdc.run()

