from sympy import symbols, Matrix
from sympy.plotting import plot3d
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



A = np.array([0, 0, 1, 1])
B = np.array([1, 0, 1, 1])
C = np.array([1, 1, 1, 1]) 
D = np.array([0, 1, 1, 1])

T = []

#plot3d(A, (x,0,10))

fig = plt.figure()
ax = fig.add_subplot(111, projection= '3d')
ax.scatter(A[0], A[1], A[2], c = 'r')
ax.scatter(B[0], B[1], B[2], c = 'g')
ax.scatter(C[0], C[1], C[2], c = 'b')
ax.scatter(D[0], D[1], D[2], c = 'y')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

