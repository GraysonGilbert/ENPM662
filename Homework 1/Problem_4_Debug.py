from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

init_printing(use_unicode=True)

# Initializing Symbols
x, y = symbols('x y')
l_1, l_2, l_3, theta_1, theta_2, theta_3, theta_dot_1, theta_dot_2, theta_dot_3 =  symbols('l_1 l_2 l_3 theta_1 theta_2 theta_3 theta_dot_1 theta_dot_2 theta_dot_3')
#x, x_dot_theta_1, x_dot_theta_2, x_dot_theta_3, y, y_dot_theta_1, y_dot_theta_2, y_dot_theta_3 = symbols('x x_dot_theta_1 x_dot_theta_2 x_dot_theta_3 y y_dot_theta_1 y_dot_theta_2 y_dot_theta_3', cls=Function)


# Robot Link Length Specifications

l_1 = 0.3
l_2 = 0.3
l_3 = 0.1

# Solving Forward Kinematics

x = (l_1 *  cos(theta_1)) + (l_2 *  cos(theta_1 + theta_2)) + (l_3 *  cos(theta_1 + theta_2 + theta_3))

x_dot_theta_1 = Derivative(x, theta_1).doit()
x_dot_theta_2 = Derivative(x, theta_2).doit()
x_dot_theta_3 = Derivative(x, theta_3).doit()

y = (l_1*sin(theta_1)) + (l_2*sin(theta_1 + theta_2)) + (l_3*sin(theta_1 + theta_2 + theta_3))

y_dot_theta_1 = Derivative(y, theta_1).doit()
y_dot_theta_2 = Derivative(y, theta_2).doit()
y_dot_theta_3 = Derivative(y, theta_3).doit()


j = Matrix([[x_dot_theta_1, x_dot_theta_2, x_dot_theta_3], [y_dot_theta_1, y_dot_theta_2, y_dot_theta_3], [1,1,1]])
theta_dot = Matrix([theta_dot_1, theta_dot_2, theta_dot_3])

# Calculating Inverse Jacobian Matrix

inverse_j = j ** -1

#pretty_print(inverse_j)
# _________________________________________________________________________________________

# Creating a list of alpa values for circle
alpha = []
total_steps = 10
step = 30/total_steps


for t in np.arange(0, 30, step):
    alpha.append(((2 * pi.evalf(5))/30) *t)

# Circle Specifications

r = .20
a = 0
b = 0

# Initialize theta values for each link of robot, starts in home position of theta_1 = theta_2 = theta_3 = 0

theta_1_vals = [0]
theta_2_vals = [0]
theta_3_vals = [0]

x_check_vals = []
y_check_vals = []
theta_check_vals = []


x_check = (l_1 *  cos(theta_1)) + (l_2 *  cos(theta_1 + theta_2)) + (l_3 *  cos(theta_1 + theta_2 + theta_3))
y_check = (l_1*sin(theta_1)) + (l_2*sin(theta_1 + theta_2)) + (l_3*sin(theta_1 + theta_2 + theta_3))
theta_check = theta_1 + theta_2 + theta_3


for i in range(0, 1):
    
    x_check_num = x_check.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i]})
    y_check_num = y_check.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i]})
    theta_check_num = theta_check.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i]})

    x_check_vals.append(x_check_num)
    y_check_vals.append(y_check_num)
    theta_check_vals.append(theta_check_num)

print(theta_check_vals)


alpha_check = ((2*pi.evalf(5))/30) * 30
#print(alpha_check)

for i in range(0, ):

    # Creating a list of X, Y, and Theta values for the circle

    x = r * cos(alpha[i]) + a
    y = r * sin(alpha[i]) + b
    theta = 0 * alpha[i]

    x_dot = ((-2 *  pi.evalf(5)) / 30) * r * sin(alpha[i])
    y_dot = ((2 * pi.evalf(5)) / 30) * r * cos(alpha[i])
    theta_dot = 0 * alpha[i]

    # Position Matrix
    x_vals = Matrix([x_dot, y_dot, theta_dot])

    sol = inverse_j * x_vals

    sol = sol.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i]})

    theta_1_vals.append(float(sol[0]) * step)
    theta_2_vals.append(float(sol[1]) * step)
    theta_3_vals.append(float(sol[2]) * step)

    pretty_print(sol)