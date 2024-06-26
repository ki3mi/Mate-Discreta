import os

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


while True:
    os.system("cls")
    print("*"*20)
    print("Ejercicios:")
    print("""          
1-> Ejercicio A
2-> Ejercicio B
3-> Ejercicio C
4-> Salir
""")
    option = int(input("-> "))
    os.system("cls")
    if option == 1:
        # caso 1 ejercicio A
        a = int(input("Ingrese la cantidad de terminos que desea: "))
        print("Ejercicio A")
        print("n términos de la serie: ",fibonacci(a))
        print("*"*20)
        x = input("*Preciona una tecla para volver al menú*")
    elif option == 2:
        #Caso 1 ejercicio B
        print("Ejercicio B")
        b = int(input("Ingrese n termino que desea: "))
        print("Ejercicio B, n término de la serie: ",n_termino(b))
        print("*"*20)    
        x = input("*Preciona una tecla para volver al menú*")
    elif option == 3:
        #Caso 1 ejercicio C
        print("Ejercicio C")
        c = int(input("Ingrese la cantidad de terminos que desea sumar: "))
        print("Ejercicio A, suma de n términos de la serie: ",suma_n_terminos(c))
        print("*"*20)    
        x = input("*Preciona una tecla para volver al menú*")
    else:
        break

    