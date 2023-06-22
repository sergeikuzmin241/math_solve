# Расчет RC Цепи для гармонического сигнала

from cmath import *
from math import degrees
from tkinter import *
from tkinter import font
from tkinter import ttk

print("Расчет RC Цепи")
f = 1000
R = int(input("Введите R " ))
C = int(input("Введите C " ))
V = 10
t = 0
w = 2*pi*f
print(w)
j = 1j
Vin = V*exp(j*w*t)
print("Входная характеристика (напряжение на входе", Vin)
Zc = 1/(j*w*C)
print("емкостное сопротивление", Zc)
I = Vin/(R+Zc)
print("ток", I)
Vc = I*Zc
print("Выходная характеристика (напряжение на выходе", Vc)
K = Vc/Vin
K, phi = polar(K)
phi = degrees(phi)
print("Комплексно передаточная функция",K)