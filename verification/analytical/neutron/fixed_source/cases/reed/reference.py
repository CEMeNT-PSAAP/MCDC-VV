import numpy as np

# Warsa, J.S., "Analytical SN solutions in heterogeneous slabs, using symbolic algebra computer programs"
# Ann. Nucl. Energy, 29(7), 851-874 (2002). DOI: 10.1016/S0306-4549(01)00080-9

# Reproduce the reference equations from Warsa (2002).


def reference():
    x = np.linspace(0.0, 8.0, 81)
    dx = x[1:] - x[:-1]
    I = len(x) - 1

    # define integral functions
    def integral_phi1(x):
        return (
            x
            - (5.96168047527760e-47 / 52.06761235859028)
            * np.sinh(52.06761235859028 * x)
            - (6.78355315350872e-56 / 62.76152118553390)
            * np.sinh(62.76152118553390 * x)
            - (7.20274049646598e-84 / 95.14161078659372)
            * np.sinh(95.14161078659372 * x)
            - (6.34541150517664e-238 / 272.5766481169758)
            * np.sinh(272.5766481169758 * x)
        )

    def integral_phi2(x):
        return (
            -(1.685808767651539e3 / 5.206761235859028) * np.exp(-5.206761235859028 * x)
            - (3.143867366942945e4 / 6.276152118553390) * np.exp(-6.276152118553390 * x)
            - (2.879977113018352e7 / 9.514161078659372) * np.exp(-9.514161078659372 * x)
            - (8.594190506002560e22 / 27.25766481169758)
            * np.exp(-27.25766481169758 * x)
            + (1.298426035202193e-36 / 27.25766481169758)
            * np.exp(27.25766481169758 * x)
            + (1.432344656303454e-13 / 9.514161078659372)
            * np.exp(9.514161078659372 * x)
            + (1.514562265056083e-9 / 6.276152118553390) * np.exp(6.276152118553390 * x)
            + (1.594431209450755e-8 / 5.206761235859028) * np.exp(5.206761235859028 * x)
        )

    def integral_phi3(x):
        return 1.105109108062394 * x

    def integral_phi4(x):
        return (
            10.0 * x
            - (0.1983746883968300 / 0.5254295183311557) * np.exp(0.5254295183311557 * x)
            - (7.824765332896027e-5 / 1.108937229227813) * np.exp(1.108937229227813 * x)
            - (9.746660212187006e-6 / 1.615640334315550) * np.exp(1.615640334315550 * x)
            - (2.895098351422132e-13 / 4.554850586269065)
            * np.exp(4.554850586269065 * x)
            + (75.34793864805979 / 0.5254295183311557) * np.exp(-0.5254295183311557 * x)
            + (20.42874998426011 / 1.108937229227813) * np.exp(-1.108937229227813 * x)
            + (7.129175418204712e2 / 1.615640334315550) * np.exp(-1.615640334315550 * x)
            + (2.716409367577795e9 / 4.554850586269065) * np.exp(-4.554850586269065 * x)
        )

    def integral_phi5(x):
        return (
            -(31.53212162577067 / 0.5254295183311557) * np.exp(-0.5254295183311557 * x)
            - (26.25911060454856 / 1.108937229227813) * np.exp(-1.108937229227813 * x)
            - (1.841223066417334e3 / 1.615640334315550) * np.exp(-1.615640334315550 * x)
            - (1.555593549394869e11 / 4.554850586269065)
            * np.exp(-4.554850586269065 * x)
            - (3.119310353653182e-3 / 0.5254295183311557)
            * np.exp(0.5254295183311557 * x)
            - (6.336401143340483e-7 / 1.108937229227813) * np.exp(1.108937229227813 * x)
            - (3.528757679361232e-8 / 1.615640334315550) * np.exp(1.615640334315550 * x)
            - (4.405514335746888e-18 / 4.554850586269065)
            * np.exp(4.554850586269065 * x)
        )

    # initialize containers
    a_values = np.zeros(I)
    b_values = np.zeros(I)
    phi_values = np.zeros(I)
    x_values = np.zeros(I)

    # calculate phi bin-averaged phi values
    for i, a in enumerate(x[:-1]):
        b = x[i + 1]

        if a < 2:
            phi_val = integral_phi1(b) - integral_phi1(a)
        elif a < 3:
            phi_val = integral_phi2(b) - integral_phi2(a)
        elif a < 5:
            phi_val = integral_phi3(b) - integral_phi3(a)
        elif a < 6:
            phi_val = integral_phi4(b) - integral_phi4(a)
        else:
            phi_val = integral_phi5(b) - integral_phi5(a)

        phi_values[i] = phi_val / dx[i] / 100
        a_values[i] = a
        b_values[i] = b
        x_values[i] = (a_values[i] + b_values[i]) / 2

    return x_values, phi_values
