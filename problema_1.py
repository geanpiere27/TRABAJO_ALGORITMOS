# Ejercicio Uno
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automatica
# el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el
# precio de la entrada. Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y si es mayor 
# de 18 deberá pagar 10 soles.

def calcular_precio_entrada(edad):
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 5
    else:
        return 10

edad = int(input("Por favor, ingresa la edad del cliente: "))
precio = calcular_precio_entrada(edad)
print("El precio de entrada es:", precio, "soles")

# En esta versión, eliminamos la estructura try y except y asumimos que el usuario ingresará un valor válido para la edad. 
# Esto simplifica el código, pero es importante recordar que no se manejarán errores si el usuario ingresa un valor no numérico.