import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D

#Ранг матрицы
a = np.array([[7, 2, 1], [3, 4, 5], [6, 8, 10]])
print(a)
print('ранг матрицы а: ', np.linalg.matrix_rank(a))