import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D

a = np.array([[7, 2], [3, 4]])
print(a) # Вывод матрицы
print('обратная матрица a: \n', np.linalg.inv(a))
print('находим исходную матрицу а от обратной матрицы: \n', np.linalg.inv(np.linalg.inv(a)))