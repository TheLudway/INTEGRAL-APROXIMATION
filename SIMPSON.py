import fractions
import matplotlib.pyplot as plt


def Simpson(n, a, b, dic = {}, x_g = [], y_g = [], Resultado = 0, graph = True):
    """ Aproximación de la integral"""
    delta_x = (b-a) / (n-1)  # CALCULA EL DELTA X
    for i in range(n):
        """Prueba si el valor ingresado es una fracción y agrega el """
        x = input("Valor x de la pareja ordenada: ")
        try:
            if not x.isnumeric():
                x = fractions.Fraction(x)
        except ValueError:
            (x + "No se encuentra en el Dominio")
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
    contador = 1
    for i in dic.values():
        contador += 1
        if i != dic.get(b):
            if contador % 2 == 0:
                Resultado += i * 4
            else:
                Resultado += i * 2
        else:
            Resultado += dic.get(b)
    Resultado *= delta_x / 3
    redondear = round(Resultado, 2)
    print(redondear)
    if graph == True:
        plt.plot(x_g, y_g, color = (32/255, 32/255, 32/255))
        plt.title(f"El resultado de la aproximación es {redondear}")
        plt.xlabel("Eje x")
        plt.ylabel("Eje y")
        plt.fill_between(x_g, y_g, color = (32/255, 32/255, 32/255))
        plt.show()
    return Resultado

Simpson(13, 0, 43200)

"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
"""