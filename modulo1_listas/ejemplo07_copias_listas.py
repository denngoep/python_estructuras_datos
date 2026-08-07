# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 1 - Listas
# Ejemplo 7: Copias de listas

# Se crea una lista original.

lista_original = ["Python", "Java", "C#", "JavaScript"]

print("Lista original:")

# Se crea una copia utilizando el método copy()
lista_copia = lista_original.copy()

print("\nCopia de la lista:")
print(lista_copia)

# Se modifica la lista copiada. 
lista_copia.append("Kotlin")

print("\nLista original después de modificar la copia:")
print(lista_original)

print("\nLista copiada después de agregar 'Kotlin' :")
print(lista_copia)

# ¿Qué hace este programa?

# Este programa muestra cómo crear una copia independiente de una lista 
# utilizando el método copy()
# Al modificar la copia, la lista original permanece igual. 