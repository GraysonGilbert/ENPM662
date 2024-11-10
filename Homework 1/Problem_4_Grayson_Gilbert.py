from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

init_printing(use_unicode=True)

# Initializing Symbols
x, y = symbols('x y')
l_1, l_2, l_3, theta_1, theta_2, theta_3, theta_dot_1, theta_dot_2, theta_dot_3 =  symbols('l_1 l_2 l_3 theta_1 theta_2 theta_3 theta_dot_1 theta_dot_2 theta_dot_3')

# Robot Link Length Specifications

l_1 = 0.5
l_2 = 0.5
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

theta = theta_1 + theta_2 + theta_3

# Jacobian Matrix
j = Matrix([[x_dot_theta_1, x_dot_theta_2, x_dot_theta_3], [y_dot_theta_1, y_dot_theta_2, y_dot_theta_3], [1,1,1]])
theta_dot = Matrix([theta_dot_1, theta_dot_2, theta_dot_3])


# _________________________________________________________________________________________

# Circle Specifications

r = .20
a = 0
b = 0

# Creating a list of alpha values for circle
alpha = []
total_steps = 500
step = 30/total_steps

time = np.linspace(0, 30, total_steps)

for t in np.arange(0, 30, step):
    alpha.append(((2 * pi.evalf(5))/30) *t)

# Creating a list of X, Y, and Theta values for the circle

x_circle = []
y_circle = []
x_dot = []
y_dot = []

for i in range(0, len(alpha)):

    x_circle.append(r * cos(alpha[i]) + a)
    y_circle.append(r * sin(alpha[i]) + b)
    theta = theta_1 + theta_2 + theta_3

    x_dot.append(((-2 *  pi.evalf(5)) / 30) * r * sin(alpha[i]))
    y_dot.append(((2 * pi.evalf(5)) / 30) * r * cos(alpha[i]))

    theta_dot = 0


# Initialize theta values for each link of robot

theta_1_vals = [0.3535]
theta_2_vals = [-0.707]
theta_3_vals = [.3535]

x_check_vals = []
y_check_vals = []
theta_check_vals = []


x_check = (l_1 *  cos(theta_1)) + (l_2 *  cos(theta_1 + theta_2)) + (l_3 *  cos(theta_1 + theta_2 + theta_3))
y_check = (l_1*sin(theta_1)) + (l_2*sin(theta_1 + theta_2)) + (l_3*sin(theta_1 + theta_2 + theta_3))
theta_check = theta_1 + theta_2 + theta_3


x_dot_vals = []
y_dot_vals = []


# Solving Inverse Kinemtaic Equations

for i in range(0, total_steps):



    # Position Matrix
    x_vals = Matrix([x_dot[i], y_dot[i], theta_dot])

    j_sub = j.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i]})
   
    
  
    inverse_j = j_sub ** -1
   
   
    q = inverse_j * x_vals
    
    
    theta_1_vals.append(theta_1_vals[i-1] + (float(q[0]) * step))
    theta_2_vals.append(theta_2_vals[i-1] + (float(q[1]) * step))
    theta_3_vals.append(theta_3_vals[i-1] + (float(q[2]) * step))

    x_dot_vals.append(q[0])
    y_dot_vals.append(q[1])



# Verifying Solution by Plugging in calculated theta values
for i in range(0, total_steps):

    x_check_num = x_check.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i]})
    y_check_num = y_check.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i]})
    theta_check_num = theta_check.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i]})

    x_check_vals.append(x_check_num)
    y_check_vals.append(y_check_num)
    theta_check_vals.append(theta_check_num)




# Plotting Relevant Information

# Plot of Theta Values Vs. Time
plt.figure(1)
plt.title('Theta Values Over Time')
plt.plot(time, theta_1_vals[1:], label='theta 1')
plt.plot(time, theta_2_vals[1:], label='theta 2')
plt.legend()

# Plot of End Effector Trajectory
plt.figure(2)
plt.title('End Effector Trajectory')
plt.plot(y_check_vals, x_check_vals)


# Plot of Joint Velocities

plt.figure(3)
plt.title('Joint Velocity Over Time')
plt.plot(time, x_dot_vals, label='x joint velocity')
plt.plot(time, y_dot_vals, label='y joint velocity')
plt.legend()
plt.plot()


plt.show()


