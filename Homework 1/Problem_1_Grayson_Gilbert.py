import matplotlib.pyplot as plt
import math
import numpy as np

# Robot Dimensions

wheel_dia = 0.6
wheel_r = wheel_dia / 2
wheel_base = 1.2

# Initial Conditions for the Problem

duration = 25
step = 1000
time_arr = np.linspace(0, duration, num = step)

# Scenario 1:

# wl -> left wheel angular velocity, wr -> right wheel angular velocity
wl_1 = 2
wr_1 = 1

x_dot_1 = np.array([])
x_1 = np.array([0])
y_dot_1 = np.array([])
y_1 = np.array([0])


theta_dot_1 = (wheel_r / wheel_base) * (wr_1 - wl_1)

theta_1 = theta_dot_1 * time_arr

for num in range(0, len(time_arr)):

    x_dot_1 = np.append(x_dot_1, (wheel_r / 2) * (wl_1 + wr_1) * math.cos(theta_1[num]))
    y_dot_1 = np.append(y_dot_1, (wheel_r / 2) * (wl_1 + wr_1) * math.sin(theta_1[num]))

for num in range(0, len(time_arr)-1):
        
    x_1 = np.append(x_1, x_1[num -1] + x_dot_1[num] * (duration/step))
    y_1 = np.append(y_1, y_1[num -1] + y_dot_1[num] * (duration/step))



# Scenario 2:

# wl -> left wheel angular velocity, wr -> right wheel angular velocity
wl_2 = 1
wr_2 = 2

x_dot_2 = np.array([])
x_2 = np.array([0])
y_dot_2 = np.array([])
y_2 = np.array([0])

theta_dot_2 = (wheel_r / wheel_base) * (wr_2 - wl_2)
theta_2 = theta_dot_2 * time_arr


for num in range(0, len(time_arr)):

    x_dot_2 = np.append(x_dot_2, (wheel_r / 2) * (wl_2 + wr_2) * math.cos(theta_2[num]))
    y_dot_2 = np.append(y_dot_2, (wheel_r / 2) * (wl_2 + wr_2) * math.sin(theta_2[num]))

for num in range(0, len(time_arr)-1):
        
    x_2 = np.append(x_2, x_2[num -1] + x_dot_2[num] * (duration/step))
    y_2 = np.append(y_2, y_2[num -1] + y_dot_2[num] * (duration/step))


# Plotting Scenario 1:
plt.plot(x_1, y_1, label = 'Scenario 1')
# Plotting Scenario 2:
plt.plot(x_2, y_2, label = 'Scenario 2')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Trajectories of 2 Wheeled Dif. Drive Robots')
plt.legend()

plt.show()