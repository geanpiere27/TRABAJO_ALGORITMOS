# Ejercicio Once
# Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números (que puedan ser decimales) y calcule su suma, 
# mostrar por terminal la suma de los números introducidos.

cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))
if cantidad_numeros <= 0:
    print("Error: Debes introducir al menos un número.")
else:
    suma = 0
    for i in range(cantidad_numeros):
        numero = float(input("Introduce el número {}: ".format(i + 1)))
        suma += numero

    print("La suma de los números introducidos es:", suma)


#Este programa pregunta al usuario cuántos números va a introducir. Luego, utiliza un bucle for para pedir esos números uno por uno.
# Cada número se suma al total acumulado en la variable suma. Finalmente, muestra la suma de los números introducidos por el usuario.