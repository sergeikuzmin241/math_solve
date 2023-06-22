import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D
#Массив(матрица) а:
a = np.array([[7, 2], [3, 4]])
print(a) # Вывод матрицы
print('определитель матрицы' , np.linalg.det(a)) # Определитель матрицы
print('a:T \n' , a.T) # транспонированная матрица
print('определитель транспонированной матрицы:' , 'det.(a.T): = ', np.linalg.det(a.T)) #Определитель транспонированной матрицы
# Нахождение исхондой матрицы от обрптной и наоборот