import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Generate data
x = np.linspace(-100, 100, 1000)
y = np.linspace(-100, 100, 1000)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("3D Plot")
plt.show()

# 2D contour plot
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='Z value')
plt.title("2D Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()