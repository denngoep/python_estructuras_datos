# MÓDULO 1 : LISTAS
# Ejemplo 2: Slicing (segmentación de listas)

# Se crea una lista con varios números.
numeros = [10, 20, 30, 40, 50, 60, 70]

# Se imprime la lista completa. 
print("Lista completa:")
print(numeros)

# Se obtiene los tres primeros elementos. 
print("\nPrimeros tres elementos:")
print(numeros[:3])

# Se obtiene los elementos desde la posición 2 hasta la 5.
print("\nElementos desde la posición 2 hasta la 5:")
print(numeros[2:6])

# Se obtiene los últimos tres elementos. 
print("\nÚltimo tres elementos:")
print(numeros[-3:])

# Se obtiene una copia completa de la lista.
print("\nCopia completa de la lista")
print(numeros[:])

# Se obtiene la lista saltando de dos en dos.
print("\nElementos de dos en dos:")
print(numeros[::2])

# Se imprime la llista en orden inverso. 
print("\nLista invertida:")
print(numeros[::-1])

# ¿Qué hace este programa?

# Este programa demuestra cómo tilizar el slicing para:
# - Extraer una parte de una lista.
# - Obtener los primeros y últimos elementos.
# - Crear una copia de una lista. 
# - Recorrer elementos con saltos.
# - Invertir una lista utilizando slicing.
