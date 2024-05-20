# Ejercicio Seis
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de la imagen adjunta.
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

## SOLUCION DOS: 
#altura = int(input("Por favor, ingresa la altura del triángulo rectángulo: "))

#for i in range(1, altura + 1):
#    print("*" * i)

#Este programa solicita al usuario que ingrese la altura del triángulo rectángulo y luego utiliza un bucle for para imprimir cada línea del triángulo.
# En cada iteración del bucle, se imprime una cadena formada por el carácter "*" repetido "i" veces, donde "i" es el número de la iteración actual.
# Esto generará un triángulo con una base que coincide con la altura ingresada.