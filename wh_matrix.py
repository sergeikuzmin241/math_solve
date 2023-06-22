#Смена размера матриц
# я хрен его почему не работает

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D

mass = np.array(1, 10, 1)
print(mass)
mass = mass.reshape(3,3)
print(mass)
mass = mass.reshape(1,9)
print(mass)