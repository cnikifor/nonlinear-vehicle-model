# Christina Nikiforidou, Last edited in 05/23/2023

# This class contains the Tire Magic Formula, developed by Bakker and Pacejka, for the estimation of the (lateral)
# forces experienced between the tires and the ground w.r.t. to the slip angle. The constants B, C, D, and E are
# extracted experimentally. The subscripts "f" and "r" represent "front" and "rear", respectively.

import numpy as np


class TireModel:
    """
    The magic formula is used to extract lateral tire force data given the slip
    angle that each tire experiences. Based on empirical data, we define values
    for the constants used in the formula.
    """

    B_f = 11.275  # Stiffness factor
    C_f = 1.56  # Shape factor
    D_f = -2574.7  # Peak value
    E_f = -1.999  # Curvature factor

    B_r = 18.631
    C_r = 1.56
    D_r = -1749.7
    E_r = -1.7908

    def __init__(self,
                 a_fr,  # slip angle on front right tire
                 a_fl,  # slip angle on front left tire
                 a_rr,  # slip angle on rear right tire
                 a_rl):  # slip angle on rear left tire

        self.a_front = np.asarray([a_fr, a_fl])
        self.a_rear = np.asarray([a_rr, a_rl])

    def mf_f(self):
        a_front = self.a_front

        f_front = np.zeros_like(a_front)
        f_front[0] = TireModel.D_f * np.sin(TireModel.C_f * np.arctan(TireModel.B_f * a_front[0]
                                                            - TireModel.E_f * (TireModel.B_f * a_front[0] - np.arctan(
                                                                TireModel.B_f * a_front[0]))))

        f_front[1] = TireModel.D_f * np.sin(TireModel.C_f * np.arctan(TireModel.B_f * a_front[1]
                                                            - TireModel.E_f * (TireModel.B_f * a_front[1] - np.arctan(
                                                                TireModel.B_f * a_front[1]))))

        return f_front

    def mf_r(self):
        a_rear = self.a_rear

        f_rear = np.zeros_like(a_rear)
        f_rear[0] = TireModel.D_r * np.sin(TireModel.C_r * np.arctan(TireModel.B_r * a_rear[0]
                                                           - TireModel.E_r * (TireModel.B_r * a_rear[0] - np.arctan(
                                                                TireModel.B_r * a_rear[0]))))

        f_rear[1] = TireModel.D_r * np.sin(TireModel.C_r * np.arctan(TireModel.B_r * a_rear[1]
                                                           - TireModel.E_r * (TireModel.B_r * a_rear[1] - np.arctan(
                                                                TireModel.B_r * a_rear[1]))))

        return f_rear
