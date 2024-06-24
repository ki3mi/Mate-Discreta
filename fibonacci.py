def fibonacci(n):
    valores = [0, 1]
    for i in range(1, n):
        valores.append(valores[-1] + valores[-2])
    
    valores.remove(0)
    return(valores)
def n_termino(n):
    serie = fibonacci(n)
    valor = serie[-1]
    return valor

def suma_n_terminos(n):
    lista = fibonacci(n)
    suma = sum(lista)
    return suma

y = n_termino(10)
x = fibonacci(10)
z = suma_n_terminos(10)

print(x)
print(y)
print(z)