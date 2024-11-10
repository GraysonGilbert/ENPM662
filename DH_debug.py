from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

init_printing(use_unicode=True)


# Initializing Symbols
a_1, a_2, a_3, a_4, a_5, a_6, =  symbols('a_1 a_2 a_3 a_4 a_5 a_6')
alpha_1, alpha_2, alpha_3, alpha_4, alpha_5, alpha_6 = symbols('alpha_1 alpha_2 alpha_3 alpha_4 alpha_5 alpha_6')
d_1, d_2, d_3, d_4, d_5, d_6 = symbols('d_1 d_2 d_3 d_4 d_5 d_6')
theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = symbols('theta_1 theta_2 theta_3 theta_4 theta_5 theta_6')


a_1 = 0
a_2 = 737.31
a_3 = 387.8
a_4 = 0
a_5 = 0
a_6 = 0

alpha_1 = -(pi/2)
alpha_2 = 0
alpha_3 = 0
alpha_4 = -(pi/2)
alpha_5 = (pi/2)
alpha_6 = 0

d_1 = 183.3
d_2 = 0
d_3 = 0
d_4 = 95.5
d_5 = 115.5
d_6 = 121.8

theta_1 = 0
theta_2 = -(pi/2)
theta_3 = 0
theta_4 = -(pi/2)
theta_5 = -(pi/2)
theta_6 = 0

# Constructing Matrices

A_1 = Matrix([[cos(theta_1), -cos(alpha_1)*sin(theta_1), sin(alpha_1)*sin(theta_1), a_1*cos(theta_1)],
             [sin(theta_1), cos(alpha_1)*cos(theta_1), -sin(alpha_1)*cos(theta_1), a_1*sin(theta_1)],
             [0, sin(alpha_1), cos(alpha_1), d_1],
             [0, 0, 0, 1]])

A_2 = Matrix([[cos(theta_2), -cos(alpha_2)*sin(theta_2), sin(alpha_2)*sin(theta_2), a_2*cos(theta_2)],
             [sin(theta_2), cos(alpha_2)*cos(theta_2), -sin(alpha_2)*cos(theta_2), a_2*sin(theta_2)],
             [0, sin(alpha_2), cos(alpha_2), d_2],
             [0, 0, 0, 1]])


print("A_1:")
pretty_print(A_1)

print("A_2:")
pretty_print(A_2)

ans = A_1 * A_2

pretty_print(ans)