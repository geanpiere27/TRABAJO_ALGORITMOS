# Ejercicio quince
# Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
 
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# 
# Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos.

def fibonacci(n):
    # Inicializamos los primeros dos números de la secuencia
    fibonacci_seq = [0, 1]
    
    # Generamos los siguientes números de la secuencia hasta alcanzar el número deseado
    while len(fibonacci_seq) < n:
        # Calculamos el siguiente número como la suma de los dos últimos números
        next_num = fibonacci_seq[-1] + fibonacci_seq[-2]
        # Añadimos el siguiente número a la secuencia
        fibonacci_seq.append(next_num)
    
    return fibonacci_seq

# Probemos la función con los primeros 12 números de la secuencia de Fibonacci
n = 12
resultado = fibonacci(n)
print("La sucesión de Fibonacci hasta el término", n, "es:", resultado)


#Este código define una función `fibonacci(n)` que genera los primeros `n` números de la sucesión de Fibonacci.
# Comienza con los números iniciales (0 y 1) y luego calcula cada número subsiguiente como la suma de los dos números anteriores.
# La función devuelve una lista con la secuencia de Fibonacci hasta el término especificado.

# SOLUCION 2:

a, b = 0, 1
while a < 100:
    print(a, end=', ')
    a, b = b, a + b


#Este código inicializa dos variables, `a` y `b`, con los dos primeros números de la secuencia de Fibonacci. Luego, utilizando un bucle `while`,
# genera los números de Fibonacci hasta que el número generado sea menor que 100. En cada iteración del bucle, `a` y `b` se actualizan para
# generar el siguiente número de Fibonacci.