import numpy as np
from scipy.integrate import quad
from scipy.special import exp1

# Parameters
SigmaT = 1.0
v = 1.0
T = 5.0

# Point-wise solution


def phi_(y, t):
    if y > v * t:
        return 0.0
    else:
        return (
            1.0
            / T
            * (
                SigmaT * y * (exp1(SigmaT * v * t) - exp1(SigmaT * y))
                + np.e ** (-SigmaT * y)
                - y / (v * t) * np.e ** (-SigmaT * v * t)
            )
        )


def phi_Y(t, y1, y2):
    return quad(phi_, y1, y2, args=(t))[0] / (y2 - y1)


def reference(y, t):
    y_mid = 0.5 * (y[:-1] + y[1:])
    dt = t[1:] - t[:-1]
    K = len(dt)
    J = len(y_mid)

    phi = np.zeros([K, J])
    for k in range(K):
        for j in range(J):
            y1 = y[j]
            y2 = y[j + 1]
            t1 = t[k]
            t2 = t[k + 1]
            phi[k, j] = quad(phi_Y, t1, t2, args=(y1, y2))[0] / (t2 - t1)
            # phi[k, j] = quad(phi_, y1, y2, args=(t[k + 1]))[0] / (y2 - y1)

    return phi
