# Производная функции
# хрен его почему не работает

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D


x = Symbol("x")
diff((4*x**2 + 3), x, oo) 