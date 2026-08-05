import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.045694],
	['U238',0.001335],
	['C0',7.456e-05],
	['Fe54',1.054438e-06],
	['Fe56',1.65524216e-05],
	['Fe57',3.822676e-07],
	['Fe58',5.08728e-08],
	['W180',1.095984e-09],
	['W182',2.420298e-07],
	['W183',1.30696092e-07],
	['W184',2.79841248e-07],
	['W186',2.59656876e-07]])
# Material Name: Polyethylene
# S(a,b): c_H_in_CH2 (Not Implemented)
m2 = mcdc.material(nuclides=[
	['C0',0.03929],
	['H1',0.078579]])
# Material Name: Titanium
m3 = mcdc.material(nuclides=[
	['Ti46',0.00467214],
	['Ti47',0.0042134208],
	['Ti48',0.0417491104],
	['Ti49',0.0030637912000000002],
	['Ti50',0.0029335376],
	['Al27',0.0010151]])
# Material Name: Aluminium
m4 = mcdc.material(nuclides=[
	['Al27',0.059154],
	['Mn55',0.00038519],
	['Si28',0.000160359744616],
	['Si29',8.142610292e-06],
	['Si30',5.367645092e-06],
	['Fe54',5.963069000000001e-06],
	['Fe56',9.36074308e-05],
	['Fe57',2.1618038e-06],
	['Fe58',2.8769640000000003e-07]])
# Material Name: Steel
m5 = mcdc.material(nuclides=[
	['Fe54',0.00484006915],
	['Fe56',0.07597873478],
	['Fe57',0.0017546803300000002],
	['Fe58',0.00023351574000000003],
	['C0',0.00040815],
	['Si28',0.000413954472744],
	['Si29',2.1019427028e-05],
	['Si30',1.3856100228e-05],
	['Mn55',0.00042492],
	['Cr50',2.9261402500000003e-06],
	['Cr52',5.642770205e-05],
	['Cr53',6.398448449999999e-06],
	['Cr54',1.5927092500000001e-06]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=-21.24, bc='vacuum')
s2 = mcdc.surface('plane-z', z=-20.75, bc='interface')
s3 = mcdc.surface('plane-z', z=-18.78, bc='interface')
s4 = mcdc.surface('plane-z', z=-18.29, bc='interface')
s5 = mcdc.surface('plane-z', z=-16.3, bc='interface')
s6 = mcdc.surface('plane-z', z=-15.81, bc='interface')
s7 = mcdc.surface('plane-z', z=-13.84, bc='interface')
s8 = mcdc.surface('plane-z', z=-13.35, bc='interface')
s9 = mcdc.surface('plane-z', z=-11.36, bc='interface')
s10 = mcdc.surface('plane-z', z=-10.87, bc='interface')
s11 = mcdc.surface('plane-z', z=-8.9, bc='interface')
s12 = mcdc.surface('plane-z', z=-8.41, bc='interface')
s13 = mcdc.surface('plane-z', z=-6.42, bc='interface')
s14 = mcdc.surface('plane-z', z=-5.93, bc='interface')
s15 = mcdc.surface('plane-z', z=-3.96, bc='interface')
s16 = mcdc.surface('plane-z', z=-3.47, bc='interface')
s17 = mcdc.surface('plane-z', z=-1.48, bc='interface')
s18 = mcdc.surface('plane-z', z=-0.99, bc='interface')
s19 = mcdc.surface('plane-z', z=0.0, bc='interface')
s20 = mcdc.surface('plane-z', z=1.26, bc='interface')
s21 = mcdc.surface('plane-z', z=1.46, bc='interface')
s22 = mcdc.surface('plane-z', z=2.06, bc='interface')
s23 = mcdc.surface('plane-z', z=2.24, bc='interface')
s24 = mcdc.surface('plane-z', z=2.73, bc='interface')
s25 = mcdc.surface('plane-z', z=4.72, bc='interface')
s26 = mcdc.surface('plane-z', z=5.21, bc='interface')
s27 = mcdc.surface('plane-z', z=7.18, bc='interface')
s28 = mcdc.surface('plane-z', z=7.67, bc='interface')
s29 = mcdc.surface('plane-z', z=9.66, bc='interface')
s30 = mcdc.surface('plane-z', z=10.15, bc='interface')
s31 = mcdc.surface('plane-z', z=12.12, bc='interface')
s32 = mcdc.surface('plane-z', z=12.61, bc='interface')
s33 = mcdc.surface('plane-z', z=14.6, bc='interface')
s34 = mcdc.surface('plane-z', z=15.09, bc='interface')
s35 = mcdc.surface('plane-z', z=17.06, bc='interface')
s36 = mcdc.surface('plane-z', z=17.55, bc='interface')
s37 = mcdc.surface('plane-z', z=19.54, bc='interface')
s38 = mcdc.surface('plane-z', z=20.03, bc='interface')
s39 = mcdc.surface('plane-z', z=22.0, bc='interface')
s40 = mcdc.surface('plane-z', z=22.49, bc='vacuum')
s50 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.6, bc='interface')
s51 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=9.995, bc='interface')
s52 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=12.0, bc='interface')
s53 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=13.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s2 & -s51, fill=m4)
c2 = mcdc.cell(+s2 & -s3 & -s51, fill=m2)
c3 = mcdc.cell(+s3 & -s4 & -s51, fill=m4)
c4 = mcdc.cell(+s4 & -s5 & -s51, fill=m1)
c5 = mcdc.cell(+s5 & -s6 & -s51, fill=m4)
c6 = mcdc.cell(+s6 & -s7 & -s51, fill=m2)
c7 = mcdc.cell(+s7 & -s8 & -s51, fill=m4)
c8 = mcdc.cell(+s8 & -s9 & -s51, fill=m1)
c9 = mcdc.cell(+s9 & -s10 & -s51, fill=m4)
c10 = mcdc.cell(+s10 & -s11 & -s51, fill=m2)
c11 = mcdc.cell(+s11 & -s12 & -s51, fill=m4)
c12 = mcdc.cell(+s12 & -s13 & -s51, fill=m1)
c13 = mcdc.cell(+s13 & -s14 & -s51, fill=m4)
c14 = mcdc.cell(+s14 & -s15 & -s51, fill=m2)
c15 = mcdc.cell(+s15 & -s16 & -s51, fill=m4)
c16 = mcdc.cell(+s16 & -s17 & -s51, fill=m1)
c17 = mcdc.cell(+s17 & -s18 & -s51, fill=m4)
c18 = mcdc.cell(+s18 & -s19 & +s50 & -s51, fill=m2)
c19 = mcdc.cell(+s18 & -s19 & -s50, fill=mvoid)
c20 = mcdc.cell(+s19 & -s20 & -s51, fill=mvoid)
c21 = mcdc.cell(+s20 & -s23 & -s51, fill=m2)
c22 = mcdc.cell(+s23 & -s24 & -s51, fill=m4)
c23 = mcdc.cell(+s24 & -s25 & -s51, fill=m1)
c24 = mcdc.cell(+s25 & -s26 & -s51, fill=m4)
c25 = mcdc.cell(+s26 & -s27 & -s51, fill=m2)
c26 = mcdc.cell(+s27 & -s28 & -s51, fill=m4)
c27 = mcdc.cell(+s28 & -s29 & -s51, fill=m1)
c28 = mcdc.cell(+s29 & -s30 & -s51, fill=m4)
c29 = mcdc.cell(+s30 & -s31 & -s51, fill=m2)
c30 = mcdc.cell(+s31 & -s32 & -s51, fill=m4)
c31 = mcdc.cell(+s32 & -s33 & -s51, fill=m1)
c32 = mcdc.cell(+s33 & -s34 & -s51, fill=m4)
c33 = mcdc.cell(+s34 & -s35 & -s51, fill=m2)
c34 = mcdc.cell(+s35 & -s36 & -s51, fill=m4)
c35 = mcdc.cell(+s36 & -s37 & -s51, fill=m1)
c36 = mcdc.cell(+s37 & -s38 & -s51, fill=m4)
c37 = mcdc.cell(+s38 & -s39 & -s51, fill=m2)
c38 = mcdc.cell(+s39 & -s40 & -s51, fill=m4)
c39 = mcdc.cell(+s20 & -s21 & +s51 & -s52, fill=m5)
c40 = mcdc.cell(+s20 & -s22 & +s52 & -s53, fill=m5)
c41 = mcdc.cell(+s21 & -s22 & +s51 & -s52, fill=mvoid)
c42 = mcdc.cell(+s1 & -s20 & +s51 & -s53, fill=mvoid)
c43 = mcdc.cell(+s22 & -s40 & +s51 & -s53, fill=mvoid)
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

