# Ejercicio catorce
# Tenemos la pantalla del móvil bloqueada. Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. Tenemos hasta 3 intentos.
# Simula el proceso con Python. En caso de acceder, lanza al usuario login correcto. Sino, llamando ala policía.


PIN_SECRETO = "1234"

for _ in range(3):
    intento = input("Ingrese el PIN: ")
    if intento == PIN_SECRETO:
        print("¡Desbloqueo exitoso! Acceso concedido.")
        break
else:
    print("Se han agotado los intentos. ¡Llamando a la policía!")

# En este código, se define el PIN_SECRETO y luego se utiliza un bucle for para permitir al usuario hasta tres intentos
# de ingresar el PIN correcto. Si el usuario ingresa el PIN correcto, se imprime un mensaje de acceso concedido y el bucle
# se interrumpe con la instrucción break. Si el usuario no ingresa el PIN correcto después de tres intentos, se imprime un
# mensaje indicando que se han agotado los intentos y se simula una llamada a la policía utilizando un else junto con el bucle for.