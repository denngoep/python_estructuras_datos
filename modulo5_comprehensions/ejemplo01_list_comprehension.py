# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 5 - Comprehensions
# Ejemplo 1: List Comprehension

# Se crea una lista con números del 1 al 10.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Lista original:")
print(numeros)

# Se crea una nueva lista con el cuadrado
# de cada número utilizando List Comprehension.
cuadrados = [numero ** 2 for numero in numeros]

print("\nCuadrados de los números:")
print(cuadrados)

# ¿Qué hace este programa?
#
# Este programa muestra cómo crear una nueva lista
# utilizando List Comprehension.
#
# En lugar de utilizar un ciclo for tradicional,
# Python permite construir listas en una sola línea.