# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 4 - Conjuntos
# Ejemplo 2: Agregar y eliminar elementos

# Se crea un conjunto con algunos lenguajes.
lenguajes = {"Python", "Java", "C#"}

print("Conjunto inicial:")
print(lenguajes)

# add() agrega un nuevo elemento.
lenguajes.add("JavaScript")

print("\nDespués de add():")
print(lenguajes)

# update() agrega varios elementos.
lenguajes.update({"PHP", "Kotlin"})

print("\nDespués de update():")
print(lenguajes)

# remove() elimina un elemento.
lenguajes.remove("Java")

print("\nDespués de remove():")
print(lenguajes)

# discard() elimina un elemento si existe.
# Si no existe, no genera error.
lenguajes.discard("Swift")

print("\nDespués de discard('Swift'):")
print(lenguajes)

# ¿Qué hace este programa?
#
# Este programa muestra cómo:
# - Agregar un elemento con add().
# - Agregar varios elementos con update().
# - Eliminar un elemento con remove().
# - Eliminar un elemento con discard().
#
# La diferencia es que discard() no genera error
# si el elemento no existe.