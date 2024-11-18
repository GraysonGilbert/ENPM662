# PROBLEM 1

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
theta_2_vals = [0.1]
theta_3_vals = [-.383]
theta_4_vals = [0.283]
theta_5_vals = [0.0001]
theta_6_vals = [0]

x_end_pos = []
y_end_pos = []
z_end_pos = []

# Initialize x,yz, velocities
x_dot = [-0.001]
y_dot = [0]
z_dot = []
alpha_dot = [0]
beta_dot = [0]
gamma_dot = [0]

step_tracker = 0

# Straight Line Down Path from Home Position

vertical_steps = 400
vert_step = 40/vertical_steps

home_vert_z_dot = np.zeros(vertical_steps)
home_vert_x_dot = np.zeros(vertical_steps)

home_ramp_up_vert = int(vertical_steps * 0.1)
home_ramp_down_vert = int(vertical_steps * 0.9)


for i in range(0, vertical_steps):

    if i < home_ramp_up_vert:
        home_vert_z_dot[i] = home_vert_z_dot[i-1] - (0.00513/home_ramp_up_vert) * 2

    if i >= home_ramp_up_vert and i < home_ramp_down_vert:
        home_vert_z_dot[i] = -0.00512 * 2

    if i >= home_ramp_down_vert and i < vertical_steps:
        home_vert_z_dot[i] = home_vert_z_dot[i-1] + ((0.00506/home_ramp_up_vert)) * 2
    
    if i >= vertical_steps:
        home_vert_z_dot[i] = 0



# Specifying Cirlce Information

r = .05

circle_total_steps = 400
circle_step = 40/circle_total_steps

# Creating a list of alpha values for circle
alpha = []

for t in np.arange(0, 40, circle_step):
    alpha.append(((pi.evalf(5))/40) *t)

# Make circle_x_dot, cirlce_z_dot arrays
x_circle = []
z_circle = []

circle_x_dot = []
circle_z_dot = []

for i in range(0, len(alpha)):
    x_circle.append(r * cos(alpha[i]))
    z_circle.append(r * sin(alpha[i]))
    circle_x_dot.append(((2 * pi.evalf(5)) / 40) * r * sin(alpha[i]))
    circle_z_dot.append(((2 * pi.evalf(5)) / 40) * r * cos(alpha[i]))


# Straight Line Down Path

vertical_steps = 400
vert_step = 40/vertical_steps

vert_z_dot = np.zeros(vertical_steps)
vert_x_dot = np.zeros(vertical_steps)

ramp_up_vert = int(vertical_steps * 0.1)
ramp_down_vert = int(vertical_steps * 0.9)

for i in range(0, vertical_steps):

    if i < ramp_down_vert:
        vert_z_dot[i] = -0.0013 * 2

    if i >= ramp_down_vert and i < vertical_steps:
        vert_z_dot[i] = vert_z_dot[i-1] + ((0.0013/ramp_up_vert)) * 2
    
    if i >= vertical_steps:
        vert_z_dot[i] = 0



# Straight Line Across Path

horizontal_steps = 400
horiz_step = 40/horizontal_steps

horiz_step_x_dot = np.zeros(horizontal_steps)
horiz_step_z_dot = np.zeros(horizontal_steps)

ramp_up_horiz = int(horizontal_steps * 0.1)
ramp_down_horiz = int(horizontal_steps * 0.9)

for i in range(0, horizontal_steps):

    if i < ramp_up_horiz:
        horiz_step_x_dot[i] = horiz_step_x_dot[i-1] + ((0.0028/ramp_up_horiz)) * 2

    if i >= ramp_up_horiz and i < ramp_down_horiz:
        horiz_step_x_dot[i] = (0.0028) * 2

    if i >= ramp_down_horiz and i < horizontal_steps:
        horiz_step_x_dot[i] = horiz_step_x_dot[i-1] - ((0.0028/ramp_up_horiz)) * 2
    
    if i >= vertical_steps:
        horiz_step_x_dot[i] = 0



# Straight Line Up Path

vert_up_z_dot = np.zeros(vertical_steps)
vert_up_x_dot = np.zeros(vertical_steps)

rev_vert_z_dot = vert_z_dot[::-1]

for i in range(0, vertical_steps):
    vert_up_z_dot[i] = (-1) * rev_vert_z_dot[i]


# Final Combined X_dot and Z_dot trajectories

z_dot_combined = home_vert_z_dot.tolist() + circle_z_dot + vert_z_dot.tolist() + horiz_step_z_dot.tolist() + vert_up_z_dot.tolist()
x_dot_combined = home_vert_x_dot.tolist() + circle_x_dot + vert_x_dot.tolist() + horiz_step_x_dot.tolist() + vert_up_x_dot.tolist()

#__________________________________________________________________________________________

# Moving from Home Position to Start Point

print("Drawing Vertical Line Down from Home Position")
for i in range(0, vertical_steps):

    x_vals = Matrix([0, 0, home_vert_z_dot[i], 0, 0, 0])

    J_sub = J.subs({theta_1: theta_1_vals[step_tracker + i], theta_2: theta_2_vals[step_tracker + i], theta_3: theta_3_vals[step_tracker + i], theta_4: theta_4_vals[step_tracker + i], theta_5: theta_5_vals[step_tracker + i], theta_6: theta_6_vals[step_tracker + i]})

    inv_J = J_sub.pinv()

    q_dot = inv_J * x_vals


    # Collecting Calculated Joint Angles

    theta_1_vals.append(theta_1_vals[step_tracker + i-1] + (float(q_dot[0]) * vert_step))
    theta_2_vals.append(theta_2_vals[step_tracker + i-1] + (float(q_dot[1]) * vert_step))
    theta_3_vals.append(theta_3_vals[step_tracker + i-1] + (float(q_dot[2]) * vert_step))
    theta_4_vals.append(theta_4_vals[step_tracker + i-1] + (float(q_dot[3]) * vert_step))
    theta_5_vals.append(theta_5_vals[step_tracker + i-1] + (float(q_dot[4]) * vert_step))
    theta_6_vals.append(theta_6_vals[step_tracker + i-1] + (float(q_dot[5]) * vert_step))


step_tracker += vertical_steps

# Drawing Semi Circle

print("Drawing Half Circle")
for i in range(0, circle_total_steps):

    x_vals = Matrix([-circle_x_dot[i], y_dot[0], circle_z_dot[i], alpha_dot[0], beta_dot[0], gamma_dot[0]])

    J_sub = J.subs({theta_1: theta_1_vals[step_tracker + i], theta_2: theta_2_vals[step_tracker + i], theta_3: theta_3_vals[step_tracker + i], theta_4: theta_4_vals[step_tracker + i], theta_5: theta_5_vals[step_tracker + i], theta_6: theta_6_vals[step_tracker + i]})

    inv_J = J_sub.pinv()

    q_dot = inv_J * x_vals


    # Collecting Calculated Joint Angles

    theta_1_vals.append(theta_1_vals[step_tracker + i-1] + (float(q_dot[0]) * circle_step))
    theta_2_vals.append(theta_2_vals[step_tracker + i-1] + (float(q_dot[1]) * circle_step))
    theta_3_vals.append(theta_3_vals[step_tracker + i-1] + (float(q_dot[2]) * circle_step))
    theta_4_vals.append(theta_4_vals[step_tracker + i-1] + (float(q_dot[3]) * circle_step))
    theta_5_vals.append(theta_5_vals[step_tracker + i-1] + (float(q_dot[4]) * circle_step))
    theta_6_vals.append(theta_6_vals[step_tracker + i-1] + (float(q_dot[5]) * circle_step))

step_tracker += circle_total_steps

# Drawing Vertical Line Down

print("Drawing Vertical Line Down")
for i in range(0, vertical_steps):

    x_vals = Matrix([0, 0, vert_z_dot[i], 0, 0, 0])

    J_sub = J.subs({theta_1: theta_1_vals[step_tracker + i], theta_2: theta_2_vals[step_tracker + i], theta_3: theta_3_vals[step_tracker + i], theta_4: theta_4_vals[step_tracker + i], theta_5: theta_5_vals[step_tracker + i], theta_6: theta_6_vals[step_tracker + i]})

    inv_J = J_sub.pinv()

    q_dot = inv_J * x_vals


    # Collecting Calculated Joint Angles

    theta_1_vals.append(theta_1_vals[step_tracker + i-1] + (float(q_dot[0]) * vert_step))
    theta_2_vals.append(theta_2_vals[step_tracker + i-1] + (float(q_dot[1]) * vert_step))
    theta_3_vals.append(theta_3_vals[step_tracker + i-1] + (float(q_dot[2]) * vert_step))
    theta_4_vals.append(theta_4_vals[step_tracker + i-1] + (float(q_dot[3]) * vert_step))
    theta_5_vals.append(theta_5_vals[step_tracker + i-1] + (float(q_dot[4]) * vert_step))
    theta_6_vals.append(theta_6_vals[step_tracker + i-1] + (float(q_dot[5]) * vert_step))


step_tracker += vertical_steps

#Drawing Horizontal Line Across

print("Drawing Horizontal Line Across")
for i in range(0, vertical_steps):

    x_vals = Matrix([horiz_step_x_dot[i], 0, 0, 0, 0, 0])

    J_sub = J.subs({theta_1: theta_1_vals[step_tracker + i], theta_2: theta_2_vals[step_tracker + i], theta_3: theta_3_vals[step_tracker + i], theta_4: theta_4_vals[step_tracker + i], theta_5: theta_5_vals[step_tracker + i], theta_6: theta_6_vals[step_tracker + i]})

    inv_J = J_sub.pinv()

    q_dot = inv_J * x_vals


    # Collecting Calculated Joint Angles

    theta_1_vals.append(theta_1_vals[step_tracker + i-1] + (float(q_dot[0]) * horiz_step))
    theta_2_vals.append(theta_2_vals[step_tracker + i-1] + (float(q_dot[1]) * horiz_step))
    theta_3_vals.append(theta_3_vals[step_tracker + i-1] + (float(q_dot[2]) * horiz_step))
    theta_4_vals.append(theta_4_vals[step_tracker + i-1] + (float(q_dot[3]) * horiz_step))
    theta_5_vals.append(theta_5_vals[step_tracker + i-1] + (float(q_dot[4]) * horiz_step))
    theta_6_vals.append(theta_6_vals[step_tracker + i-1] + (float(q_dot[5]) * horiz_step))

step_tracker += horizontal_steps

# Drawing Vertical Line Up, Completing Shape

print("Drawing Vertical Line Up")
for i in range(0, vertical_steps):

    x_vals = Matrix([0, 0, vert_up_z_dot[i], 0, 0, 0])

    J_sub = J.subs({theta_1: theta_1_vals[step_tracker + i], theta_2: theta_2_vals[step_tracker + i], theta_3: theta_3_vals[step_tracker + i], theta_4: theta_4_vals[step_tracker + i], theta_5: theta_5_vals[step_tracker + i], theta_6: theta_6_vals[step_tracker + i]})

    inv_J = J_sub.pinv()

    q_dot = inv_J * x_vals


    # Collecting Calculated Joint Angles

    theta_1_vals.append(theta_1_vals[step_tracker + i-1] + (float(q_dot[0]) * vert_step))
    theta_2_vals.append(theta_2_vals[step_tracker + i-1] + (float(q_dot[1]) * vert_step))
    theta_3_vals.append(theta_3_vals[step_tracker + i-1] + (float(q_dot[2]) * vert_step))
    theta_4_vals.append(theta_4_vals[step_tracker + i-1] + (float(q_dot[3]) * vert_step))
    theta_5_vals.append(theta_5_vals[step_tracker + i-1] + (float(q_dot[4]) * vert_step))
    theta_6_vals.append(theta_6_vals[step_tracker + i-1] + (float(q_dot[5]) * vert_step))

#_________________________________________________________________________________________________

# Verifying Solution by Plugging in calculated theta values
total_steps = vertical_steps + circle_total_steps + vertical_steps + horizontal_steps + vertical_steps
time = np.linspace(0, 200, total_steps)

for i in range(0, total_steps):

    # Plugging Calculated Joint Angles Back into Forward Kinematic Equation

    end_pos = A_6_wrt_0.subs({theta_1: theta_1_vals[i], theta_2: theta_2_vals[i], theta_3: theta_3_vals[i], theta_4: theta_4_vals[i], theta_5: theta_5_vals[i], theta_6: theta_6_vals[i]})

    x_pos = end_pos[0, 3]
    y_pos = end_pos[1, 3]
    z_pos = end_pos[2, 3]


    x_end_pos.append(x_pos)
    y_end_pos.append(y_pos)
    z_end_pos.append(z_pos)


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
plt.xlabel('time (s)')
plt.ylabel('theta (rad)')
plt.legend()


# Plot of End Effector Trajectory
plt.figure(2)
plt.title('End Effector Trajectory')
plt.plot(x_end_pos, z_end_pos)
plt.xlabel('X Position (m)')
plt.ylabel('Z Position (m)')

# Plot of just the shape after reaching start point

plt.figure(3)
plt.title('End Effector Trajectory (After reaching start point)')
plt.plot(x_end_pos[400:], z_end_pos[400:])
plt.xlabel('X Position (m)')
plt.ylabel('Z Position (m)')

plt.figure(4)
plt.title("Z_dot and X_dot Throughout Entire Path")
plt.plot(time, z_dot_combined, label='z dot')
plt.plot(time, x_dot_combined, label='x dot')
plt.xlabel('time (s)')
plt.ylabel('theta_dot (rad/s)')
plt.legend()


# Plot of X_dot and Z_dot while drawing Semi Circle

#plt.figure(4)
#plt.title("X_dot and Z_dot while drawing Semi Circle")
#plt.plot(time[:circle_total_steps], circle_x_dot, label='x dot')
#plt.plot(time[:circle_total_steps], circle_z_dot, label='z dot')
#plt.legend()

# Plot of Vertical Line Down Z_dot
#plt.figure(5)
#plt.title("vertical line down z dot")
#plt.plot(time[:vertical_steps], vert_z_dot, label='z dot')
#plt.legend()

# Plot of Horizontal Line Across Z_dot
#plt.figure(6)
#plt.title("horizontal line across x dot")
#plt.plot(time[:horizontal_steps], horiz_step_x_dot, label='x dot')
#plt.legend()

# Plot of Vertical Line Up Z_dot
#plt.figure(7)
#plt.title("vertical line up z dot")
#plt.plot(time[:vertical_steps], vert_up_z_dot, label='z dot')
#plt.legend()

# Plot of Moving from Home Position to Start Point
#plt.figure(8)
#plt.title("vertical line down from home position z dot")
#lt.plot(time[:vertical_steps], home_vert_z_dot, label='z dot')
#plt.legend()

# Plot of X_dot and Z_dot trajectories

plt.show()
