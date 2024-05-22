# Ejercicio Dieciocho
# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas
# coincidan.

while (contraseña := input("Ingrese la contraseña: ")) != input("Vuelva a ingresar la contraseña: "):
    print("Las contraseñas no coinciden. Inténtelo de nuevo.")
print("¡Las contraseñas coinciden!")

#Este programa solicitará al usuario ingresar una contraseña y luego la misma contraseña nuevamente.
# Si las dos contraseñas coinciden, el programa imprimirá "Contraseña confirmada." y saldrá del bucle.
# Si las contraseñas no coinciden, imprimirá "Las contraseñas no coinciden. Inténtelo de nuevo."
# y volverá a solicitar las contraseñas al usuario. El bucle continuará ejecutándose hasta que se ingrese correctamente la contraseña dos
# veces seguidas.

