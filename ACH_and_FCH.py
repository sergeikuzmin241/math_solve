# подключение библиотек
from cmath import *
from tkinter import *
from canvas import *
from pylance import *


# Параметры
j=1j                      #
canvas_width = 600        #
canvas_height = 400       #
x0 = 40                   #
y0 = 360                  #
y0A = 360                 #
y0F = 200                 #
xm = 580                  #
ym = 20                   #
dx = 2                    #
dash_size = 6             #

root_color = "thistle"    #
btn_width = 8             #
fm = 1                    #

f = 1000                  #            
w = 2*pi*f                #

var_induct = 1000
var_capas = 10000
print('Переменные объявлены!')
# Функции
# расчитать частоту резонанса


def calc_resfred():
    L = var_induct / 1000
    C = var_capas / 100000000000
    Fr = int(1/(2*pi*sqrt(L*C).real))
    print(Fr)

calc_resfred()
# нарисовать оси координат
def draw_achaxes():
    pass
    #canvas.create_line

#a = np.linspace(1, 10, 100)
#print(a)

#Допилилить
