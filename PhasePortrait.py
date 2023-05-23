from Vehicle import VehicleModel
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import optimize
import numpy as np
import seaborn as sns
sns.set()

beta = np.linspace(-0.5, 0.5, 20)
r = np.linspace(-0.5, 0.5, 20)

BETA, R = np.meshgrid(beta, r)

t = 0

u, v = np.zeros(BETA.shape), np.zeros(R.shape)

NI, NJ = BETA.shape


def pp(yvec, time):
    sideslip, yaw = yvec

    # Initialize Parameters of "vehicle" class:
    vehicle = VehicleModel(sideslip,
                           yaw,
                           1,
                           1.,
                           0.015,
                           10)

    return vehicle.eom(time)


for i in range(NI):
    for j in range(NJ):
        x = BETA[i, j]
        y = R[i, j]
        yprime = pp([x, y], t)
        u[i, j] = yprime[0]
        v[i, j] = yprime[1]

Q = plt.quiver(BETA, R, u, v, color='r')

plt.xlabel(r'Sideslip angle, $ \beta $ [rad]')
plt.ylabel(' Yaw rate, r [rad/s]')
plt.title(r'$ v=10m/s, \delta=0.015rad $')

k = 1
val = np.linspace(-0.5, 0.5, 15)
for y20 in val:
    for y10 in val:
        tspan = np.linspace(0, 0.5, 100)
        y0 = [y10, y20]
        ys = odeint(pp, y0, tspan)
        plt.plot(ys[:, 0], ys[:, 1], '-b', linewidth=1, zorder=k)
        k += 1


def sys(yvec):
    sideslip, yaw = yvec

    # Initialize Parameters of "vehicle" class:
    vehicle = VehicleModel(sideslip,
                           yaw,
                           1.0,
                           1.,
                           0.015,
                           10)

    return vehicle.eom(t)


fp = np.zeros([3, 2])
fp[0, :] = optimize.fsolve(sys, np.array([0, 0]))
fp[1, :] = optimize.fsolve(sys, np.array([-0.05, 0]))
fp[2, :] = optimize.fsolve(sys, np.array([0.1, 0]))

plt.scatter(fp[0, 0], fp[0, 1], zorder=k+1, s=100, alpha=0.8, label='stable', c='forestgreen')
plt.scatter(fp[1:, 0], fp[1:, 1], zorder=k + 1, s=100, alpha=0.8, label='unstable')
plt.xlim(-0.5, 0.5)
plt.ylim(-0.5, 0.5)

plt.interactive(False)
plt.legend(loc='lower left').set_zorder(k + 2)
plt.show()
