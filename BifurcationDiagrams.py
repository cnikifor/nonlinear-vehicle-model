from Vehicle import VehicleModel
from scipy import optimize
from matplotlib import rcParams
import matplotlib.pyplot as plt
import warnings
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style("darkgrid")
warnings.filterwarnings('error')
rcParams['figure.figsize'] = 6, 5

t = 0


def ctrl_sys(yvec, velocity):
    beta, r = yvec

    # Initialize Parameters of "vehicle" class:
    vehicle = VehicleModel(beta,
                           r,
                           0,
                           0,
                           0.015,
                           velocity)

    return vehicle.eom(t)


mu = np.linspace(5, 40, 30)

NI = mu.shape[0]
fp = np.empty((0, 4), float)

for i in range(NI):
    v = mu[i]

    try:
        fp1 = optimize.fsolve(ctrl_sys, np.array([0, 0]), args=v)
        fp = np.append(fp, np.reshape(np.append(np.array([v, 'stable']), fp1), (1, 4)), axis=0)
    except RuntimeWarning:
        pass

    try:
        fp2 = optimize.fsolve(ctrl_sys, np.array([-0.05, 0]), args=v)
        fp = np.append(fp, np.reshape(np.append(np.array([v, 'unstable']), fp2), (1, 4)), axis=0)
    except RuntimeWarning:
        pass

    try:
        fp3 = optimize.fsolve(ctrl_sys, np.array([0.05, 0]), args=v)
        fp = np.append(fp, np.reshape(np.append(np.array([v, 'unstable']), fp3), (1, 4)), axis=0)
    except RuntimeWarning:
        pass

d = {"Velocity": np.asarray(fp[:, 0], dtype=float), "Stability": fp[:, 1], "Beta": np.asarray(fp[:, 2], dtype=float),
     "Yaw Rate": np.asarray(fp[:, 3], dtype=float)}
df = pd.DataFrame(d)
df = df.drop([53, 56, 59])
df = df.drop_duplicates(subset=['Beta', 'Yaw Rate'], keep='last')

plt.figure(0)
g = sns.scatterplot(data=df, x="Velocity", y="Beta", hue="Stability", hue_order=['stable', 'unstable'],
                    palette="deep", alpha=0.85, s=100, linewidth=0, marker='^')
plt.title(r'Fixed points for side slip angle, $ \beta$')
plt.xlabel(r'Velocity, v')
plt.ylabel(r'Side slip angle, $ \beta$')

plt.figure(1)
h = sns.scatterplot(data=df, x="Velocity", y="Yaw Rate", hue="Stability", hue_order=['stable', 'unstable'],
                    palette="deep", alpha=0.85, s=100, linewidth=0, marker='^')
plt.title('Fixed points for yaw velocity, r')
plt.xlabel(r'Velocity, v')
plt.ylabel('Yaw velocity, r')

plt.interactive(False)
plt.show()
