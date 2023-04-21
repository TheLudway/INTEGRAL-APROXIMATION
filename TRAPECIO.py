import fractions
import matplotlib.pyplot as plt


def Trapezoidal(n, a, b, dic={}, x_g = [], y_g = [], Resultado = 0, graph = True):
    delta_x = (b - a) / (n - 1)
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
            (y + "No se encuentra en el dominio")
        doubleofy = float(y)
        dic.update({doubleofx:doubleofy})
        x_g.append(doubleofx)
        y_g.append(doubleofy)
    Resultado += dic.get(a)
    dic.pop(a)
    Resultado += dic.get(b)
    dic.pop(b)
    for i in dic.values():
        Resultado += i*2
    Resultado *= delta_x/2
    redondear = round(Resultado, 2)
    print(redondear)
    if graph == True:
        plt.plot(x_g, y_g, color = (32/255, 32/255, 32/255))
        plt.title(f"El resultado de la aproximación es {redondear}")
        plt.xlabel("Eje x")
        plt.ylabel("Eje y")
        plt.fill_between(x_g, y_g, color = (21/255, 101/255, 192/255))
        plt.show()
    return Resultado


Trapezoidal



"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
"""