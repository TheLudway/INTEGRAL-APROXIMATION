import matplotlib.pyplot as plt
import fractions 
from openpyxl import  Workbook, load_workbook
from openpyxl.utils import get_column_letter


def Riemann_L(n, b, a, dic={}, x_g=[], y_g=[], Resultado = 0, graph = True):
    delta_x = (b - a) / (n-1)
    for i in range(n):
        x = input("Valor x de la pareja ordenada: ")
        try:
            if not x.isnumeric():
                x = fractions.Fraction(x)
        except ValueError:
            (x + "No se encuentra en el dominio")
        doubleofx = float(x)
        y = input("Valor y de la pareja ordenada: ")
        try:
            if not y.isnumeric():
                y = fractions.Fraction(y)
        except ValueError:
            (y + "No es un número")
        doubleofy = float(y)
        dic.update({doubleofx:doubleofy})
        x_g.append(doubleofx)
        y_g.append(doubleofy)
    dic.pop(b)
    for i in dic.values():
        Resultado += i
    Resultado *= delta_x
    print(Resultado)
    if graph == True:
        plt.plot(x_g, y_g, color = (32/255, 32/255, 32/255))
        plt.title("Título")
        plt.xlabel("Coordenada x")
        plt.ylabel("Coordenada y")
        plt.show()

Riemann_L(13, 43200, 0, graph=False)
"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
"""