def puntaje(palabra):
    score = 0
    puntos = {}
    puntos["A"] = 1
    puntos["B"] = 3
    puntos["C"] = 3
    puntos["D"] = 2
    puntos["E"] = 1
    puntos["F"] = 4
    puntos["G"] = 2
    puntos["H"] = 4
    puntos["I"] = 1
    puntos["J"] = 8
    puntos["K"] = 5
    puntos["L"] = 1
    puntos["M"] = 3
    puntos["N"] = 1
    puntos["O"] = 1
    puntos["P"] = 3
    puntos["Q"] = 10
    puntos["R"] = 1
    puntos["S"] = 1
    puntos["T"] = 1
    puntos["U"] = 1
    puntos["V"] = 4
    puntos["W"] = 4
    puntos["X"] = 8
    puntos["Y"] = 4
    puntos["Z"] = 10

    for c in palabra:
        score += puntos[c.upper()]
    return score


cadena = input("Ingrese una palabra: \n")

while (cadena!="exit"):
    print(puntaje(cadena))
    cadena = input("Ingrese una palabra: \n")