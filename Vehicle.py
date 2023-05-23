# Christina Nikiforidou, Last edited in 05/23/2023

# This class contains the vehicle's equations of motion, based on the Bicycle Model. The Bicycle model considers the
# front and rear axles to be represented as single wheels, and it assumes the lateral load transfer and roll to be
# negligible. This class contains the equations of motion for a bicycle model during a transient turn.

import numpy as np
from TireModel import TireModel


class VehicleModel:
    """
    q is [beta, r],
    where beta is the body sideslip angle and r is the yaw rate
    of a four-wheel vehicle system.
    """

    m = 1500  # vehicle mass [kg]
    I_z = 3000  # vehicle yaw moment of inertia [kg m2]
    a_f = 1.20  # distance from front axle to vehicle CG [m]
    a_r = 1.30  # distance from rear axle to vehicle CG [m]
    t_f = 1.29  # front track width [m]
    t_r = t_f  # rear track width [m]

    def __init__(self,
                 beta,
                 r,
                 beta_0,  # initial body sideslip angle [rad]
                 r_0,  # initial yaw rate [rad/s]
                 delta_f,  # front steer angle [rad]
                 v):  # vehicle speed [m/s]

        self.q = np.asarray([beta, r])
        self.beta_0 = beta_0
        self.r_0 = r_0
        self.delta_f = delta_f
        self.v = v
        self.params = (self.beta_0, self.r_0, self.delta_f, self.v)

    ########### Equations of Motion ###########

    def eom(self, t):
        """Governing equations of the system's motion during cornering"""
        (beta_0, r_0, delta_f, v) = self.params
        q = self.q

        a_fr = np.arctan((v * np.sin(q[0]) + VehicleModel.a_f * q[1]) /
                         (v * np.cos(q[0]) - VehicleModel.t_f * q[1] / 2)) - delta_f  # front right slip angle [rad]
        a_fl = np.arctan((v * np.sin(q[0]) + VehicleModel.a_f * q[1]) /
                         (v * np.cos(q[0]) + VehicleModel.t_f * q[1] / 2)) - delta_f  # front left slip angle [rad]
        a_rr = np.arctan((v * np.sin(q[0]) - VehicleModel.a_r * q[1]) /
                         (v * np.cos(q[0]) - VehicleModel.t_r * q[1] / 2))  # rear right slip angle [rad]
        a_rl = np.arctan((v * np.sin(q[0]) - VehicleModel.a_r * q[1]) /
                         (v * np.cos(q[0]) + VehicleModel.t_r * q[1] / 2))  # rear left slip angle [rad]

        # Initialize Parameters of "tire" class:
        tire = TireModel(a_fr,
                         a_fl,
                         a_rr,
                         a_rl)

        [f_fr, f_fl] = tire.mf_f()
        [f_rr, f_rl] = tire.mf_r()

        dqdt = np.zeros_like(q)
        dqdt[0] = (f_fr * np.cos(q[0] - delta_f) + f_fl * np.cos(q[0] - delta_f) + f_rr *
                   np.cos(q[0]) + f_rl * np.cos(q[0])) / VehicleModel.m / v - q[1]
        dqdt[1] = ((f_fr + f_fl) * np.cos(delta_f) * VehicleModel.a_f + (f_fr - f_fl) *
                   np.sin(delta_f) * VehicleModel.t_f / 2 - (f_rr + f_rl) * VehicleModel.a_r) / VehicleModel.I_z

        return dqdt
