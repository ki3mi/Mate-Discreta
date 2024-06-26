import os
def factorial(n):
    if n == 0:
        return(1)
    else:
        return n * factorial(n-1)

def combinatoria(a, b):
    data = factorial(a)/(factorial(b)*factorial(a-b))
    return data

def partidos(n):
    partidos = 2*(combinatoria(n, 2)) + combinatoria(8, 2)
    return(partidos)

while True:
    os.system("cls")
    n = int(input("Ingrese la cantidad de equipos: "))
    print(f"El número de partidos a jugar en total: ",int(partidos(n)))
    print("")
    print("**Datos separados**")
    print(f"El número de partidos a jugar para {n} equipos son (ida y vuelta): ",int(2*(combinatoria(n, 2))))
    print(f"El número de partidos a jugar para los 8 mejores equipos: ",int(combinatoria(8, 2)))
    x = input("*Preciona una tecla para volver al menú*")
