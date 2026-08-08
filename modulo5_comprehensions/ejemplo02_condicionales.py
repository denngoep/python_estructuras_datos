# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 5 - Comprehensions
# Ejemplo 2: Comprehensions con condicionales

# Se crea una lista con números del 1 al 20.
numeros = list(range(1, 21))

print("Lista original:")
print(numeros)

# Se crea una nueva lista con los números pares.
pares = [numero for numero in numeros if numero % 2 == 0]

print("\nNúmeros pares:")
print(pares)

# Se crea una nueva lista con los números mayores que 10.
mayores_diez = [numero for numero in numeros if numero > 10]

print("\nNúmeros mayores que 10:")
print(mayores_diez)

# ¿Qué hace este programa?
#
# Este programa muestra cómo utilizar condiciones
# dentro de una List Comprehension.
#
# Se filtran únicamente los números pares y los
# números mayores que 10.
#
# Esto permite crear listas nuevas aplicando
# condiciones en una sola línea.

