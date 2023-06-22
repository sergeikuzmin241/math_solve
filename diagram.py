# Векторная диаграмма для цепи трехфазного тока

# Библиотеки
from cmath import *
from tkinter import *
from tkinter import font
from tkinter import ttk

from sympy import root

# Переменные
Am = 310              # Амплитуда фазного напряжения
Fi1 = 0               # Начальные фазы напряжений
Fi2 = 2*pi/3
Fi3 = -2*pi/3

x_c = 300             # Координаты центра координат
y_c = 300
a_max = 240           # Максимальное значение геометрической величины

# цвет  элементов офрмления
root_color = "thistle"
ax_color = "blue"
u_color = "black"

# Вспомогательные переменные
btn_with = 14         # размер кнопок
# Общие функции
# Нарисовать комплексное число
def draw_val(z):
    re = z.real
    im = z.imag
    dx = re*a_max/Am
    dy = im*a_max/Am
    x = x_c + dx
    y = y_c - dy
    Canvas.create_line(x_c,y_c,x,y,fill = u_color,arrow = LAST)  #Закончил здесь
