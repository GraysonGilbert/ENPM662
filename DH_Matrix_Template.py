from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

init_printing(use_unicode=True)


# Initializing Symbols
l1, l2, l3, i4 = symbols('l1 l2 l3 i4')
a_5 =  symbols('a_5')
alpha_5 = symbols('alpha_5')
d_5 = symbols('d_5')
theta_5 = symbols('theta_5')



a_5 = 0
alpha_5 = 0
d_5 = l3 + i4
theta_5 = 0





A_5 = Matrix([[cos(theta_5), -cos(alpha_5)*sin(theta_5), sin(alpha_5)*sin(theta_5), a_5*cos(theta_5)],
             [sin(theta_5), cos(alpha_5)*cos(theta_5), -sin(alpha_5)*cos(theta_5), a_5*sin(theta_5)],
             [0, sin(alpha_5), cos(alpha_5), d_5],
             [0, 0, 0, 1]])


pretty_print(simplify(A_5))
