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


n = int(input("Ingrese la cantidad de equipos: "))
print(f"El número de partidos a jugar para {n} equipos son: ",int(partidos(n)))