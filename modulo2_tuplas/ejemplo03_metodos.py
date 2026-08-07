# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 2 - Tuplas
# Ejemplo 3: Métodos de las tuplas

# Se crea una tupla con varios números.
numeros = (5, 8, 3, 8, 2, 8, 10)

print("Tupla completa")
print(numeros)

# count() cuenta cuántas veces aparece un elemento. 
print("\nCantidad de veces que aparece el número 8:")
print(numeros.count(8))

# index() devuelve la posición de la primera aparición.
print("\nPosición del número 3:")
print(numeros.index(3))

# Se muestra la cantidad de elementos de la tupla.
print("\nCantidad de elementos:")
print(len(numeros))

# ¿Qué hace el programa?

# Este programa muestra los principales métodos disponibles
# para las tuplas.

# count() -> Cuenta cuántas veces aparece un elemento.
# index() -> Devuelve la posición de la primera aparición.
# len() -> Devuelve la cantidad de elementos.
#
# Las tuplas tienen pocos métodos porque son inmutables.
