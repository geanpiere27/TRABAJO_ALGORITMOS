# Ejercicio Diez
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece 
# la letra en la frase.

frase = input("Por favor, ingresa una frase: ")
letra = input("Ahora, ingresa una letra: ")

contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1

print("La letra", letra, "aparece", contador, "veces en la frase.")


#Este programa solicita al usuario que ingrese una frase y una letra. Luego, utiliza un bucle for para iterar sobre cada caracter de la frase.
# Si el caracter coincide con la letra ingresada por el usuario, aumenta el contador en 1. Al final,
# muestra el número de veces que aparece la letra en la frase.