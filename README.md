# nonlinear-vehicle-model
Nonlinear stability analysis of a vehicle model during transient cornering, through the production of bifurcation diagrams and phase portraits.

# Description
This project aims to explore the stability behavior of a vehicle model during a transient cornering maneuver based on different parameter inputs, such as the front steering angle or the vehicle velocity. The vehicle system is modeled as a four-wheel model where lateral load transfer and roll are neglected. This model is utilized to derive the equations for both the sideslip and yaw rate of the chassis, while the estimation of the tire forces is based on lateral force carpet plots. These plots represent experimental data on tire performance that can be approximated using the Magic Formula developed by Bakker and Pacejka. The primary objective of this project is to create phase portraits of the non-linear vehicle system and bifurcation diagrams of the system’s fixed points under various control parameters. Through this approach, the project assesses vehicle handling in the non-linear region of performance.

This project is using a simple four-wheel model which is founded on the simpler bicycle model. In the equation formulation, all the individual tire forces and slip angles are taken into account:

$$\left(\begin{array}{*{20}{c}}
\dot{\beta} \\
\dot{\psi}
\end{array} \right) =$$

$$\left(\begin{array}{*{20}{c}}
\frac{F_{fr}\cos({\beta-\delta_f}) + F_{fl}\cos({\beta-\delta_f}) + F_{rr}\cos{\beta} + F_{rl}\cos{\beta}}{mv} - \psi \\
\frac{{l_f}(F_{fr}+F_{fl})\cos{\delta_f} + \frac{t_f}{2}(F_{fr}-F_{fl})\sin{\delta_f} - {l_r}(F_{rr}+F_{rl})}{I_z}
\end{array} \right)$$

where the slip angles on each tire are determined as:

$$\alpha_{fr} = \arctan{\frac{v\sin{\beta}+l_f\psi}{v\cos{\beta}-\frac{t_f}{2}\psi}} - \delta_f$$

$$\alpha_{fl} = \arctan{\frac{v\sin{\beta}+l_f\psi}{v\cos{\beta}+\frac{t_f}{2}\psi}} - \delta_f$$

$$\alpha_{rr} = \arctan{\frac{v\sin{\beta}-l_r\psi}{v\cos{\beta}-\frac{t_r}{2}\psi}}$$

$$\alpha_{rl} = \arctan{\frac{v\sin{\beta}-l_r\psi}{v\cos{\beta}+\frac{t_r}{2}\psi}}$$

# Getting Started
## Dependencies
For the program to run, the following libraries/sub-packages need to be imported:
* [numpy](https://numpy.org/)
* [scipy.integrate](https://docs.scipy.org/doc/scipy/tutorial/integrate.html)
* [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html)
* [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
* [matplolib.rcParams](https://matplotlib.org/stable/tutorials/introductory/customizing.html)
* [pandas](https://pandas.pydata.org/)
* [seaborn](https://seaborn.pydata.org/)
* [warnings](https://docs.python.org/3/library/warnings.html)

## Executing Program
* Within the TireModel class, the user can define the factors of the Magic Tire Formula (B, C, D, E constants), which in turn impact the dynamics between the tires and the ground during a turn.
* Similarly, the parameters of the vehicle design can be determined within the VehicleModel class, such as the vehicle's mass, yaw moment of inertia, CG location, and trackwidth. 
* After constructing the tire and vehicle models, the PhasePortrait script solves the equations of motion of the vehicle model thus generating various trajectories of the system in its phase space. These phase portraits also include the equilibirum points of the system along with their stabiility classification
* The BifurcationDiagrams script plots the fixed points of the system as the vehicle vellocity or the front steering angle increase. These diagrams showcase bifurcation behaviors of the system, which can help understand stability behavior and handling. 
