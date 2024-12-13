from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

init_printing(use_unicode=True)


# Initializing Symbols
l1, l2, l3, i4 = symbols('l1 l2 l3 i4')
a_1 =  symbols('a_1')
alpha_1 = symbols('alpha_1')
d_1 = symbols('d_1')
theta_1 = symbols('theta_1')

# Initializing Symbols
l1, l2, l3, i4 = symbols('l1 l2 l3 i4')
a_2 =  symbols('a_2')
alpha_2 = symbols('alpha_2')
d_2 = symbols('d_2')
theta_2 = symbols('theta_2')

# Initializing Symbols
l1, l2, l3, i4 = symbols('l1 l2 l3 i4')
a_3 =  symbols('a_3')
alpha_3 = symbols('alpha_3')
d_3 = symbols('d_3')
#theta_2 = symbols('theta_2')

# Initializing Symbols
l1, l2, l3, i4 = symbols('l1 l2 l3 i4')
a_4 =  symbols('a_4')
alpha_4 = symbols('alpha_4')
d_4 = symbols('d_4')
#theta_3 = symbols('theta_3')

# Initializing Symbols
l1, l2, l3, i4 = symbols('l1 l2 l3 i4')
a_5 =  symbols('a_5')
alpha_5 = symbols('alpha_5')
d_5 = symbols('d_5')
theta_5 = symbols('theta_5')

a_1 = 0
alpha_1 = 0
d_1 = l1
#theta_1 = 

a_2 = 0
alpha_2 = pi/6
d_2 = 0
theta_2 = pi/2

a_3 = 0
alpha_3 = -pi/2
d_3 = l2
theta_3 = theta_2 + pi/2

a_4 = 0
alpha_4 = pi/2
d_4 = 0
theta_4 = theta_3 - pi/3

a_5 = 0
alpha_5 = 0
d_5 = l3 + i4
theta_5 = 0


A_1 = Matrix([[cos(theta_1), -cos(alpha_1)*sin(theta_1), sin(alpha_1)*sin(theta_1), a_1*cos(theta_1)],
             [sin(theta_1), cos(alpha_1)*cos(theta_1), -sin(alpha_1)*cos(theta_1), a_1*sin(theta_1)],
             [0, sin(alpha_1), cos(alpha_1), d_1],
             [0, 0, 0, 1]])

A_2 = Matrix([[cos(theta_2), -cos(alpha_2)*sin(theta_2), sin(alpha_2)*sin(theta_2), a_2*cos(theta_2)],
             [sin(theta_2), cos(alpha_2)*cos(theta_2), -sin(alpha_2)*cos(theta_2), a_2*sin(theta_2)],
             [0, sin(alpha_2), cos(alpha_2), d_2],
             [0, 0, 0, 1]])


A_3 = Matrix([[cos(theta_3), -cos(alpha_3)*sin(theta_3), sin(alpha_3)*sin(theta_3), a_3*cos(theta_3)],
             [sin(theta_3), cos(alpha_3)*cos(theta_3), -sin(alpha_3)*cos(theta_3), a_3*sin(theta_3)],
             [0, sin(alpha_3), cos(alpha_3), d_3],
             [0, 0, 0, 1]])

A_4 = Matrix([[cos(theta_4), -cos(alpha_4)*sin(theta_4), sin(alpha_4)*sin(theta_4), a_4*cos(theta_4)],
             [sin(theta_4), cos(alpha_4)*cos(theta_4), -sin(alpha_4)*cos(theta_4), a_4*sin(theta_4)],
             [0, sin(alpha_4), cos(alpha_4), d_4],
             [0, 0, 0, 1]])

A_5 = Matrix([[cos(theta_5), -cos(alpha_5)*sin(theta_5), sin(alpha_5)*sin(theta_5), a_5*cos(theta_5)],
             [sin(theta_5), cos(alpha_5)*cos(theta_5), -sin(alpha_5)*cos(theta_5), a_5*sin(theta_5)],
             [0, sin(alpha_5), cos(alpha_5), d_5],
             [0, 0, 0, 1]])

pretty_print(A_1)

pretty_print(A_2)

pretty_print(A_3)

pretty_print(A_4)

pretty_print(A_5)