# Ejercicio Dieciséis
# Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. El programa debe cumplir con los siguientes requisitos:
 
# - Debe permitir agregar nuevas tareas a la lista.
# - Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
# - Debe mostrar la lista actual de tareas pendientes.
# - Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores y salir del programa.
# El menú debe presentar las siguientes opciones:
 
# - Agregar tarea
# - Marcar tarea como completada
# - Mostrar tareas
# - Salir
tareas = []

while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        tareas.append(input("Ingrese la nueva tarea: "))
    elif opcion == "2":
        if not tareas:
            print("No hay tareas pendientes.")
        else:
            tarea_completada = tareas.pop(int(input("Ingrese el número de la tarea completada: ")) - 1)
            print(f"¡La tarea '{tarea_completada}' ha sido marcada como completada y eliminada de la lista!")
    elif opcion == "3":
        print("\nLista de tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


# Este programa permite gestionar una lista de tareas pendientes según los requisitos especificados.
# Los usuarios pueden agregar nuevas tareas, marcar tareas como completadas (lo que las elimina de la lista),
# mostrar la lista actual de tareas pendientes y salir del programa mediante un menú interactivo.

