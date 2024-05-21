# Ejercicio Trece
# Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos SAL no se apaga.
 
# Esta calculadora funciona de la siguiente manera:
# 
# - Recogemos los datos A y B
# - Si operación es 1 calcula la raíz cuadrada de la suma de A y B
# - Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
# - Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5

while True:
    print("\nBienvenido a la calculadora")
    print("Operaciones disponibles:")
    print("1. Calcular la raíz cuadrada de la suma de A y B")
    print("2. Calcular A / B")
    print("3. Calcular (A * B) / 2.5")
    print("Escribe 'SAL' para salir")

    operacion = input("Por favor, elige una operación (1, 2, 3) o 'SAL' para salir: ")

    if operacion.upper() == "SAL":
        print("Apagando la calculadora...")
        break

    if operacion not in ['1', '2', '3']:
        print("Operación no válida. Por favor, elige una opción válida.")
        continue

    A = float(input("Ingresa el valor de A: "))
    B = float(input("Ingresa el valor de B: "))

    if operacion == '1':
        resultado = (A + B) ** 0.5
        print(f"La raíz cuadrada de la suma de {A} y {B} es: {resultado}")
    elif operacion == '2':
        if B == 0:
            print("Error: No se puede dividir por cero.")
        else:
            resultado = A / B
            print(f"{A} dividido por {B} es: {resultado}")
    elif operacion == '3':
        resultado = (A * B) / 2.5
        print(f"El resultado de (A * B) / 2.5 es: {resultado}")


# Este código utiliza un bucle while para mantener la calculadora activa hasta que el usuario decida salir. Dentro del bucle,
# se presentan las opciones al usuario y se solicitan los datos A y B. Luego, se realizan las operaciones correspondientes según la
# opción seleccionada por el usuario. Si el usuario ingresa "SAL", el bucle se interrumpe y la calculadora se apaga.