# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 1 - Listas
# Ejemplo 5: Ordenar listas

# Se crea una lista con varios números desordenados. 
numeros = [45, 12, 89, 3,  27, 56]

print("Lista original:")
print(numeros)

# sort() ordena la lista de menor a mayor. 
numeros.sort()

print("\nLista ordenadas de menor a mayor:")
print(numeros)

# sort(reverse=True) ordenada de mayor a menor. 
numeros.sort(reverse=True)

print("\nLista ordenada de mayor a menor:")

print(numeros)

# reverse() invierte el orden actual de la lista. 
numeros.reverse

print("\nLista después de aplicar reverse():")
print(numeros)

# ¿Qué hace este programa?

# Este programa muestra cómo ordenar una lista utilizando:

# sort() -> Ordena ascendente.
# sort(reverse=True) -> Orden descendete. 
# reverse() -> Invierte el orden actual de la lista. 