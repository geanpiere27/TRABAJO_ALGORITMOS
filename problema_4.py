# Ejercicio Cuatro
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1, 11):
    print("Tabla de multiplicar del", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()  # Agregar una línea en blanco entre cada tabla


# En esta versión, eliminé la variable resultado y simplemente imprimí el producto directamente dentro del bucle interno.
# Esto reduce la complejidad del código y lo hace más conciso.

#1. for i in range(1, 11):`: Esto crea un bucle que recorre los números del 1 al 10 (inclusive). Este bucle exterior se encarga de iterar sobre
# cada número para el cual queremos generar una tabla de multiplicar.

#2. print("Tabla de multiplicar del", i)`: Esta línea imprime un encabezado que indica para qué número se está generando la tabla de multiplicar.
# `i` es el número actual en el bucle exterior.

#3. for j in range(1, 11):`: Este es un bucle anidado dentro del bucle exterior. Itera sobre los números del 1 al 10 (inclusive).
# Este bucle interior se encarga de calcular y mostrar cada fila de la tabla de multiplicar para el número `i`.

#4. print(i, "x", j, "=", i * j)`: Aquí se imprime cada fila de la tabla de multiplicar. Se muestra el multiplicando (`i`), el multiplicador (`j`),
# el signo de multiplicación (`x`), el resultado de la multiplicación (`i * j`).

#5. print()`: Después de imprimir todas las filas de la tabla de multiplicar para el número `i`, se imprime una línea en blanco para separar
# visualmente las tablas de multiplicar de diferentes números.

