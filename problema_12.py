# Ejercicio Doce
# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))
if cantidad_numeros <= 0:
    print("Error: Debes introducir al menos un número.")
else:
    contador_negativos = 0
    for i in range(cantidad_numeros):
        numero = float(input("Introduce el número {}: ".format(i + 1)))
        if numero < 0:
            contador_negativos += 1

    print("Has introducido", contador_negativos, "números negativos.")


#Este programa pregunta al usuario cuántos números va a introducir. Luego, utiliza un bucle for para pedir esos números uno por uno.
# Si el número ingresado es menor que cero, incrementa el contador de números negativos. Finalmente,
# muestra cuántos números negativos se han introducido