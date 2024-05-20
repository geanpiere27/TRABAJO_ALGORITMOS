# Ejercicio Ocho
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida 
# empezando por la última.

palabra = input("Por favor, ingresa una palabra: ")

for i in range(len(palabra) - 1, -1, -1):
    print(palabra[i])


#Este programa utiliza un bucle for que comienza desde el índice correspondiente a la última letra de la palabra ingresada (len(palabra) - 1)
# y se decrementa en cada iteración hasta llegar a 0. En cada iteración, imprime la letra en la posición actual. Esto permite mostrar las letras
# de la palabra ingresada por el usuario en orden inverso.