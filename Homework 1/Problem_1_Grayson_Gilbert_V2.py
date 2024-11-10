import sympy as sp
import math

# Robot Dimensions

wheel_dia = 0.6
wheel_r = wheel_dia / 2
wheel_base = 1.2

# wl -> left wheel angular velocity, wr -> right wheel angular velocity

wl_1 = 2 
wr_1 = 1

theta_dot_1 = (wheel_r / wheel_base) * (wr_1 - wl_1)


x_dot_1 = (wheel_r/2) * (wl_1 + wr_1) * sp.cos(theta)
y_dot_1 = (wheel_r/2) * (wl_1 + wr_1) * sp.sin(theta)
