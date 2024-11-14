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
a_2 = -.73731
a_3 = -.3878
a_4 = 0
a_5 = 0
a_6 = 0

alpha_1 = pi/2
alpha_2 = 0
alpha_3 = 0
alpha_4 = pi/2
alpha_5 = -pi/2
alpha_6 = 0

d_1 = .1833
d_2 = 0
d_3 = 0
d_4 = 0.0955
d_5 = .1155
d_6 = .1218

theta_1 = 0 
theta_2 = 0
theta_3 = 0
theta_4 = pi/2
theta_5 = 0
theta_6 = 0



# Constructing Matrices

A_1 = Matrix([[cos(theta_1 - pi), -cos(alpha_1)*sin(theta_1 - pi), sin(alpha_1)*sin(theta_1 - pi), a_1*cos(theta_1 - pi)],
             [sin(theta_1 - pi), cos(alpha_1)*cos(theta_1 - pi), -sin(alpha_1)*cos(theta_1 - pi), a_1*sin(theta_1 - pi)],
             [0, sin(alpha_1), cos(alpha_1), d_1],
             [0, 0, 0, 1]])

A_2 = Matrix([[cos(theta_2 - (pi/2)), -cos(alpha_2)*sin(theta_2 - (pi/2)), sin(alpha_2)*sin(theta_2 - (pi/2)), a_2*cos(theta_2 - (pi/2))],
             [sin(theta_2 - (pi/2)), cos(alpha_2)*cos(theta_2 - (pi/2)), -sin(alpha_2)*cos(theta_2 - (pi/2)), a_2*sin(theta_2 - (pi/2))],
             [0, sin(alpha_2), cos(alpha_2), d_2],
             [0, 0, 0, 1]])

A_3 = Matrix([[cos(theta_3), -cos(alpha_3)*sin(theta_3), sin(alpha_3)*sin(theta_3), a_3*cos(theta_3)],
             [sin(theta_3), cos(alpha_3)*cos(theta_3), -sin(alpha_3)*cos(theta_3), a_3*sin(theta_3)],
             [0, sin(alpha_3), cos(alpha_3), d_3],
             [0, 0, 0, 1]])

A_4 = Matrix([[cos(theta_4 - (pi/2)), -cos(alpha_4)*sin(theta_4 - (pi/2)), sin(alpha_4)*sin(theta_4 - (pi/2)), a_4*cos(theta_4 - (pi/2))],
             [sin(theta_4 - (pi/2)), cos(alpha_4)*cos(theta_4 - (pi/2)), -sin(alpha_4)*cos(theta_4 - (pi/2)), a_4*sin(theta_4 - (pi/2))],
             [0, sin(alpha_4), cos(alpha_4), d_4],
             [0, 0, 0, 1]])

A_5 = Matrix([[cos(theta_5), -cos(alpha_5)*sin(theta_5), sin(alpha_5)*sin(theta_5), a_5*cos(theta_5)],
             [sin(theta_5), cos(alpha_5)*cos(theta_5), -sin(alpha_5)*cos(theta_5), a_5*sin(theta_5)],
             [0, sin(alpha_5), cos(alpha_5), d_5],
             [0, 0, 0, 1]])

A_6 = Matrix([[cos(theta_6), -cos(alpha_6)*sin(theta_6), sin(alpha_6)*sin(theta_6), a_6*cos(theta_6)],
             [sin(theta_6), cos(alpha_6)*cos(theta_6), -sin(alpha_6)*cos(theta_6), a_6*sin(theta_6)],
             [0, sin(alpha_6), cos(alpha_6), d_6],
             [0, 0, 0, 1]])


# Calculating Transformations
A_1_wrt_0 = A_1

A_2_wrt_0 = A_1_wrt_0 * A_2

A_3_wrt_0 = A_2_wrt_0 * A_3

A_4_wrt_0 = A_3_wrt_0 * A_4

A_5_wrt_0 = A_4_wrt_0 * A_5

A_6_wrt_0 = simplify(A_5_wrt_0 * A_6)


# Collecting Z Values

Z_1 = Matrix([0, 0, 1])

Z_2 = Matrix(A_1_wrt_0.col(2)[:3])

Z_3 = Matrix(A_2_wrt_0.col(2)[:3])

Z_4 = Matrix(A_3_wrt_0.col(2)[:3])

Z_5 = Matrix(A_4_wrt_0.col(2)[:3])

Z_6 = Matrix(A_5_wrt_0.col(2)[:3])

# Collecting P Value of Final Transformation

P_6_wrt_0 = Matrix(A_6_wrt_0.col(3)[:3])

x = P_6_wrt_0[0]
y = P_6_wrt_0[1]
z = P_6_wrt_0[2]

# Calculating Partial Derivatives

#q_1_x_dot = Derivative(x, theta_1).doit()
#q_2_x_dot = Derivative(x, theta_2).doit()
#q_3_x_dot = Derivative(x, theta_3).doit()
#q_4_x_dot = Derivative(x, theta_4).doit()
#q_5_x_dot = Derivative(x, theta_5).doit()
#q_6_x_dot = Derivative(x, theta_6).doit()

#q_1_y_dot = Derivative(y, theta_1).doit()
#q_2_y_dot = Derivative(y, theta_2).doit()
#q_3_y_dot = Derivative(y, theta_3).doit()
#q_4_y_dot = Derivative(y, theta_4).doit()
#q_5_y_dot = Derivative(y, theta_5).doit()
#q_6_y_dot = Derivative(y, theta_6).doit()

#q_1_z_dot = Derivative(z, theta_1).doit()
#q_2_z_dot = Derivative(z, theta_2).doit()
#q_3_z_dot = Derivative(z, theta_3).doit()
#q_4_z_dot = Derivative(z, theta_4).doit()
#q_5_z_dot = Derivative(z, theta_5).doit()
#q_6_z_dot = Derivative(z, theta_6).doit()

# Constructing Jacobian



#J = Matrix([[q_1_x_dot, q_2_x_dot, q_3_x_dot, q_4_x_dot, q_5_x_dot, q_6_x_dot],
#            [q_1_y_dot, q_2_y_dot, q_3_y_dot, q_4_y_dot, q_5_y_dot, q_6_y_dot],
#            [q_1_z_dot, q_2_z_dot, q_3_z_dot, q_4_z_dot, q_5_z_dot, q_6_z_dot],
#            [Z_1, Z_2, Z_3, Z_4, Z_5, Z_6]])

# Problem 1 Results

#print('A1:')
#pretty_print(simplify(A_1))
#print('A2:')
#pretty_print(simplify(A_2))
#print('A3:')
#pretty_print(simplify(A_3))
#print('A4:')
#pretty_print(simplify(A_4))
#print('A5:')
#pretty_print(simplify(A_5))
#print('A6:')
#pretty_print(simplify(A_6))

print("Transformation of End Effector with respect to Base:")
pretty_print(A_6_wrt_0)