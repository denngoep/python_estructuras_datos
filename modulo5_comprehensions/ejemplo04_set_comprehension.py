# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 5 - Comprehensions
# Ejemplo 4: Set Comprehension

# Se crea una lista con varios números repetidos.
numeros = [2, 4, 6, 8, 2, 4, 10, 12, 6, 14]

print("Lista original:")
print(numeros)

# Se crea un conjunto con el cuadrado de cada número.
cuadrados = {
    numero ** 2
    for numero in numeros
}

print("\nConjunto de cuadrados:")
print(cuadrados)

# ¿Qué hace este programa?
#
# Este programa muestra cómo crear un conjunto
# utilizando Set Comprehension.
#
# Además de calcular el cuadrado de cada número,
# el conjunto elimina automáticamente los valores
# repetidos.

