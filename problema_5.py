# Ejercicio Cinco
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida
# empezando por la última.
palabra = input("Por favor, ingresa una palabra: ")

for letra in reversed(palabra):
    print(letra)


#Este programa utiliza la función reversed() para invertir el orden de las letras en la palabra ingresada por el usuario.
# Luego, utiliza un bucle for para iterar sobre las letras de la palabra invertida y las imprime una a una. De esta manera,
# las letras se muestran en orden inverso al que fueron ingresadas por el usuario.