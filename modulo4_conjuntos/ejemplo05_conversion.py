# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 4 - Conjuntos
# Ejemplo 5: Conversión entre listas y conjuntos

# Se crea una lista con elementos repetidos.
numeros_lista = [1, 2, 2, 3, 4, 4, 5, 6, 6]

print("Lista original:")
print(numeros_lista)

# Se convierte la lista en un conjunto.
numeros_conjunto = set(numeros_lista)

print("\nConjunto (sin elementos repetidos):")
print(numeros_conjunto)

# Se convierte nuevamente el conjunto en una lista.
numeros_lista_nueva = list(numeros_conjunto)

print("\nLista convertida desde el conjunto:")
print(numeros_lista_nueva)

# ¿Qué hace este programa?
#
# Este programa muestra cómo:
# - Convertir una lista en un conjunto utilizando set().
# - Eliminar automáticamente los elementos repetidos.
# - Convertir nuevamente el conjunto en una lista
#   utilizando list().
#
# Esta técnica es muy utilizada cuando se desea eliminar
# valores duplicados de una lista.