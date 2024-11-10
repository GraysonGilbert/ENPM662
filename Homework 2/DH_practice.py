from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

init_printing(use_unicode=True)


# Initializing Symbols
a_1, a_2, theta_1, theta_2 =  symbols('a_1 a_2 theta_1 theta_2')


# Constructing Matrices
A_1 = Matrix([[cos(theta_1), -sin(theta_1), 0, a_1*cos(theta_1)], 
              [sin(theta_1), cos(theta_1), 0, a_1*sin(theta_1)],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

A_2 = Matrix([[cos(theta_2), -sin(theta_2), 0, a_2*cos(theta_2)],
              [sin(theta_2), cos(theta_2), 0, a_2*sin(theta_2)],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

Expected_Answer = Matrix([[cos(theta_1 + theta_2), -sin(theta_1+theta_2), 0, a_1*cos(theta_1) + a_2*cos(theta_1+theta_2)],
                          [sin(theta_1+theta_2), cos(theta_1+theta_2), 0, a_1*sin(theta_1) + a_2*sin(theta_1 + theta_2)],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

print("A_1:")
pretty_print(A_1)
print("A_2:")
pretty_print(A_2)


# Calculating Transformations
A_final = A_1 * A_2
simp_A_final = simplify(A_final)
print("A_final")
pretty_print(simp_A_final)
