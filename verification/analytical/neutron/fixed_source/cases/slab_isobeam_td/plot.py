import matplotlib.pyplot as plt
import matplotlib.animation as animation
import h5py
import sys

from reference import reference

output = sys.argv[1]

# Reference solution
with h5py.File(output, "r") as f:
    y = f["tallies/tracklength_tally_0/grid/y"][:]
    t = f["tallies/tracklength_tally_0/grid/time"][:]
phi_ref = reference(y, t)

# Get results
with h5py.File(output, "r") as f:
    y = f["tallies/tracklength_tally_0/grid/y"][:]
    t = f["tallies/tracklength_tally_0/grid/time"][:]
    dy = y[1] - y[0]
    y_mid = 0.5 * (y[:-1] + y[1:])
    dt = t[1:] - t[:-1]
    K = len(dt)
    J = len(y_mid)

    phi = f["tallies/tracklength_tally_0/flux/mean"][:]
    phi_sd = f["tallies/tracklength_tally_0/flux/sdev"][:]

# Normalize
for k in range(K):
    phi[k] *= 0.5 / dy
    phi_sd[k] *= 0.5 / dy
for j in range(J):
    phi[:, j] /= dt
    phi_sd[:, j] /= dt

# Flux - t
fig = plt.figure()
ax = plt.axes(ylim=(5e-5, 4e-1))
ax.grid()
ax.set_xlabel(r"$y$")
ax.set_ylabel(r"Flux")
ax.set_title(r"$\bar{\phi}_{j}(t)$")
ax.set_yscale("log")
(line1,) = ax.plot([], [], "-b", label="MC")
(line2,) = ax.plot([], [], "--r", label="Ref.")
fb = ax.fill_between([], [], [], [], alpha=0.2, color="b")
text = ax.text(0.02, 0.9, "", transform=ax.transAxes)
ax.legend()


def animate(k):
    global fb
    fb.remove()
    line1.set_data(y_mid, phi[k, :])
    fb = ax.fill_between(
        y_mid,
        phi[k, :] - phi_sd[k, :],
        phi[k, :] + phi_sd[k, :],
        alpha=0.2,
        color="b",
    )
    line2.set_data(y_mid, phi_ref[k, :])
    text.set_text(r"$t \in [%.1f, %.1f]$ s" % (t[k], t[k + 1]))
    return line1, line2, text


# Uncomment to animate all time bins.
# _simulation = animation.FuncAnimation(fig, animate, frames=K)
plt.show()
