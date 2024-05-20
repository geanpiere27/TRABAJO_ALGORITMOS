# Ejercicio Nueve
# Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y muestre un mensaje cada vez que 
# un número no sea mayor que el anterior.

cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))
if cantidad_numeros <= 0:
    print("Error: Debes introducir al menos un número.")
else:
    numero_anterior = float(input("Introduce el primer número: "))
    for i in range(1, cantidad_numeros):
        numero_actual = float(input("Introduce el siguiente número: "))
        if numero_actual <= numero_anterior:
            print("El número", numero_actual, "no es mayor que el anterior.")
        numero_anterior = numero_actual


#Este programa solicita al usuario cuántos números va a introducir y luego lee esos números uno por uno.
# En cada iteración del bucle for, verifica si el número actual es menor o igual que el número anterior.
# Si es así, muestra un mensaje indicando que el número no es mayor que el anterior.
# Luego, actualiza el número anterior con el número actual para la próxima iteración.