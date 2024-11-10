from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

init_printing(use_unicode=True)


# Initializing Symbols
a_6 =  symbols('a_6')
alpha_6 = symbols('alpha_6')
d_6 = symbols('d_6')
theta_6 = symbols('theta_6')



a_6 = 0
alpha_6 = 0
d_6 = 121.8
theta_6 = 0





A_6 = Matrix([[cos(theta_6), -cos(alpha_6)*sin(theta_6), sin(alpha_6)*sin(theta_6), a_6*cos(theta_6)],
             [sin(theta_6), cos(alpha_6)*cos(theta_6), -sin(alpha_6)*cos(theta_6), a_6*sin(theta_6)],
             [0, sin(alpha_6), cos(alpha_6), d_6],
             [0, 0, 0, 1]])


pretty_print(A_6)