# Построение графика параболы

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D

k = int(input("Введите k " ))
b = int(input("Введите b " ))
x = np.arange(-10, 10)
y = k*x**2 + b
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
plt.show()