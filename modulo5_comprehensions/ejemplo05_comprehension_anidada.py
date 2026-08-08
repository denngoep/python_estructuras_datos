# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 5 - Comprehensions
# Ejemplo 5: Comprehension anidada

# Se crea una matriz (lista de listas).
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
print(matriz)

# Se crea una nueva lista con todos los elementos
# de la matriz utilizando una comprehension anidada.
numeros = [
    numero
    for fila in matriz
    for numero in fila
]

print("\nLista obtenida de la matriz:")
print(numeros)

# ¿Qué hace este programa?
#
# Este programa muestra cómo recorrer una estructura
# anidada utilizando una List Comprehension.
#
# Primero se recorre cada fila de la matriz y luego
# cada número de esa fila.
#
# El resultado es una lista con todos los elementos
# de la matriz.

