# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 1 - Listas
# Ejemplo 4: Métodos para eliminar elementos

# Se crea una lista de frutas.
frutas = ["Manzanas", "Banano", "Pera", "Uva", "Mango"]

print("Lista inicial:")
print(frutas)

# remove() elimina un elemento por su valor. 
frutas.remove("Pera")

print("\nDespués de remove('Pera'):")
print(frutas)

# pop() elimina el elemento de una posición específica.
frutas.pop(1)

print("\nDespués de pop(1):")
print(frutas)

# del elimina un elemento mediante su índice. 
del frutas[0]

print("\nDespués de el fruta[0]:")
print(frutas)

# clear() elimina todos los elementos de la lista.
frutas.clear()

print("\nDespués de clear():")
print(frutas)

# ¿Qué hace el programa?

# Este programa muestra diferentes maneras de eliminar elementos de una lista:

# remove() -> elimia un elemento por su valor. 
# pop() -> elimina un elemento por su posición.
# del -> elimina un elemento utilizando su índice. 
# clear() -> elimina todos los elementos de la lista. 
