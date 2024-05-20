# Ejercicio Tres
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número 
# separados por comas.

def mostrar_impares(numero):
    if numero <= 0:
        print("Error: Debes ingresar un número entero positivo.")
    else:
        impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
        print("Números impares hasta", numero, ":")
        print(", ".join(impares))

numero = int(input("Por favor, ingresa un número entero positivo: "))
mostrar_impares(numero)


# En esta versión, eliminamos la estructura try y except y verificamos directamente si el número ingresado es positivo o no. Si el número es positivo,
# procedemos a mostrar los números impares como se indica. Si el número no es positivo, mostramos un mensaje de error.