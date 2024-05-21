# Ejercicio Diecisiete
# Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
 
# - Verificar el saldo de su cuenta.
# - Depositar dinero en su cuenta.
# - Retirar dinero de su cuenta.
# - Salir del programa.
# El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
 
# - Verificar saldo
# - Depositar dinero
# - Retirar dinero
# - Salir

saldo = 1000

while True:
    print("\nMenú:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        saldo += cantidad
        print(f"Se ha depositado ${cantidad} correctamente.")
    elif opcion == "3":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= cantidad
            print(f"Se ha retirado ${cantidad} correctamente.")
    elif opcion == "4":
        print("¡Gracias por utilizar nuestro cajero automático!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


#Este programa de cajero automático presenta un saldo inicial predeterminado de $1000 y permite al usuario realizar operaciones como 
# verificar el saldo, depositar dinero, retirar dinero y salir del programa. Es una versión simplificada que utiliza una estructura
# de control `while` para mantener el menú activo hasta que el usuario decida salir.
