import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

a = np.linspace(0, 25, 1000)
b = np.cos(a)
c = np.sin(a)
ax.plot3D(a,b,c, 'black')

p1 = 10 * np.random.random(500)
p2 = np.cos(p1) + 0.5 * np.random.randn(500)
p3 = np.sin(p2) + 0.5 * np.random.randn(500)
ax.scatter3D(p1, p2, p3, c=p1, cmap='hsv')

plt.show()