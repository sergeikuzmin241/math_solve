# Построение графика линейной функции

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D

k = 2
b = 3
x = np.arange(-5, 6)
y = k*x + b
print(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
plt.show()