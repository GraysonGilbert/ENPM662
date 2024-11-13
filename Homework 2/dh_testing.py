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

q_1_x_dot = Derivative(x, theta_1).doit()
q_2_x_dot = Derivative(x, theta_2).doit()
q_3_x_dot = Derivative(x, theta_3).doit()
q_4_x_dot = Derivative(x, theta_4).doit()
q_5_x_dot = Derivative(x, theta_5).doit()
q_6_x_dot = Derivative(x, theta_6).doit()

q_1_y_dot = Derivative(y, theta_1).doit()
q_2_y_dot = Derivative(y, theta_2).doit()
q_3_y_dot = Derivative(y, theta_3).doit()
q_4_y_dot = Derivative(y, theta_4).doit()
q_5_y_dot = Derivative(y, theta_5).doit()
q_6_y_dot = Derivative(y, theta_6).doit()

q_1_z_dot = Derivative(z, theta_1).doit()
q_2_z_dot = Derivative(z, theta_2).doit()
q_3_z_dot = Derivative(z, theta_3).doit()
q_4_z_dot = Derivative(z, theta_4).doit()
q_5_z_dot = Derivative(z, theta_5).doit()
q_6_z_dot = Derivative(z, theta_6).doit()

# Constructing Jacobian



J = Matrix([[q_1_x_dot, q_2_x_dot, q_3_x_dot, q_4_x_dot, q_5_x_dot, q_6_x_dot],
            [q_1_y_dot, q_2_y_dot, q_3_y_dot, q_4_y_dot, q_5_y_dot, q_6_y_dot],
            [q_1_z_dot, q_2_z_dot, q_3_z_dot, q_4_z_dot, q_5_z_dot, q_6_z_dot],
            [Z_1, Z_2, Z_3, Z_4, Z_5, Z_6]])


#___________________________________________________________________________________________________________________

#Initialize Robot in Home Position
theta_1_vals = [0]
theta_2_vals = [0.01]
theta_3_vals = [-.0383]
theta_4_vals = [0.0283]
theta_5_vals = [0.0001]
theta_6_vals = [0]

x_end_pos = []
y_end_pos = []
z_end_pos = []

# Initialize x,yz, velocities
x_dot = [0]
y_dot = [0]
z_dot = []
alpha_dot = [0]
beta_dot = [0]
gamma_dot = [0]

# Setting Up Time 
z_val = []   



# Make home_2_start_z_dot array

home_2_start_steps = 300
step = 3/home_2_start_steps

ramp_up = int(home_2_start_steps * .0333334)

ramp_down = int(home_2_start_steps * .966667)

print(ramp_up)
print(ramp_down)

time = np.linspace(0, 3, home_2_start_steps)

home_2_start_z_dot = np.zeros(home_2_start_steps)

for i in range(0, home_2_start_steps):
    if i < ramp_up:
        home_2_start_z_dot[i] = home_2_start_z_dot[i-1] - ((.1724*1.71)/ramp_up)
 
    elif i >= ramp_up and i < ramp_down:
        
        home_2_start_z_dot[i] = -(.1724*1.71)

    elif i >= ramp_down and i < home_2_start_steps:
        home_2_start_z_dot[i] = home_2_start_z_dot[i-1] + ((.1724*1.71)/ramp_up)
    
    else:
   
        home_2_start_z_dot[i] = 0



# Drawing Specifications:

# Circle Specifications

r = 5
a = 0
b = 0

# Moving to start point




# Main Loop

print("entering loop")
for i in range(0, home_2_start_steps):

    x_vals = Matrix([x_dot[0], y_dot[0], home_2_start_z_dot[i], alpha_dot[0], beta_dot[0], gamma_dot[0]])

    J_sub = J.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i], theta_4: theta_4_vals[i], theta_5: theta_5_vals[i], theta_6: theta_6_vals[i]})

    inv_J = J_sub.pinv()

    q_dot = inv_J * x_vals


    # Collecting Calculated Joint Angles

    theta_1_vals.append(theta_1_vals[i-1] + (float(q_dot[0]) * step))
    theta_2_vals.append(theta_2_vals[i-1] + (float(q_dot[1]) * step))
    theta_3_vals.append(theta_3_vals[i-1] + (float(q_dot[2]) * step))
    theta_4_vals.append(theta_4_vals[i-1] + (float(q_dot[3]) * step))
    theta_5_vals.append(theta_5_vals[i-1] + (float(q_dot[4]) * step))
    theta_6_vals.append(theta_6_vals[i-1] + (float(q_dot[5]) * step))




# Verifying Solution by Plugging in calculated theta values

for i in range(0, home_2_start_steps):

    # Plugging Calculated Joint Angles Back into Forward Kinematic Equation

    end_pos = A_6_wrt_0.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i], theta_4: theta_4_vals[i], theta_5: theta_5_vals[i], theta_6: theta_6_vals[i]})

    x_pos = end_pos[0, 3]
    y_pos = end_pos[1, 3]
    z_pos = end_pos[2, 3]


    x_end_pos.append(x_pos)
    y_end_pos.append(y_pos)
    z_end_pos.append(z_pos)



print(x_end_pos[-1])
print(y_end_pos[-1])
print(z_end_pos[-1])

# Plotting Relevant Information


# Plotting Relevant Information

# Plot of Theta Values Vs. Time
plt.figure(1)
plt.title('Theta Values Over Time')
plt.plot(time, theta_1_vals[1:], label='theta 1')
plt.plot(time, theta_2_vals[1:], label='theta 2')
plt.plot(time, theta_3_vals[1:], label='theta 3')
plt.plot(time, theta_4_vals[1:], label='theta 4')
plt.plot(time, theta_5_vals[1:], label='theta 5')
plt.plot(time, theta_6_vals[1:], label='theta 6')

plt.legend()


# Plot of End Effector Trajectory
plt.figure(2)
plt.title('End Effector Trajectory')
plt.plot(x_end_pos, z_end_pos)
plt.xlim(-50,50)

plt.figure(3)

plt.title("move home 2 start z dot")
plt.plot(time, home_2_start_z_dot, label='z dot')

plt.show()
