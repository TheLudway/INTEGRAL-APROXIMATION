import matplotlib.pyplot as plt
import fractions 



def Riemann_R(n, b, a, dic={}, x_g=[], y_g=[], Resultado = 0, graph = True):
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
    dic.pop(a)
    for i in dic.values():
        Resultado += i
    Resultado *= delta_x
    redondear = round(Resultado, 2)
    print(Resultado)
    if graph == True:
        plt.plot(x_g, y_g, color = (32/255, 32/255, 32/255))
        plt.title(f"El resultado de la integral apróximada es {redondear}")
        plt.xlabel("Eje x")
        plt.ylabel("Eje y ")
        plt.show()
    return Resultado

Riemann_R(13, 43200, 0)
"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
"""