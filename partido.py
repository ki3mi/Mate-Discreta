def factorial(n):
    if n == 0:
        return(1)
    else:
        return n * factorial(n-1)

def combinatoria(n):
    partidos = 2*(factorial(n)/(factorial(2)*factorial(n-2)))
    return(partidos)

print(combinatoria(8))