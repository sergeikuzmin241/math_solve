import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, 2, 3, 4])
b = np.arange(4)
print(a)
print(b)
print('a + b: ', a+b)
print('3 * a: ', 3*a)
print('sum(b): ', b.sum())
print('min(b) :', b.min())
print('max(b) :', b.max())