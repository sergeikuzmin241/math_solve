# Решение линейоной системы au=v

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D

a = np.arange(1, 10, 1).reshape(3,3)
print(a)
a1 = np.linalg.inv(a)#обратная матрица
print(a1)
v = np.array([0,1,1])
print('\Произведение обратной матрицы а и v', np.dot(a1,v))