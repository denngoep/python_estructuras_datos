# Módulo 1: LISTAS
# Ejemplo 1: Creación y acceso a los elementos de una lista. 

# Se crea una lista llamada"tareas" con cuatro elementos. 
tareas = ["estudiar", "ejercicio", "programar", "descansar"]

# Se imprime la lista completa. 
print("Lista completa:")
print(tareas)

# Se obtiene el primer elemento de la lista utilizando el índice 0.
print("\nPrimer elemento:")
print(tareas[0])

# Se obtiene el último elemento utilizando un índice negativo.
print("\nÚltimo elemento:")
print(tareas[-1])

# Se obtiene el penúltimo elemento.
print("\nPenúltimo elemento:")
print(tareas[-2])

# Se muestra la cantidad de elementos que contiene la lista.
print("\nCantidad de elementos:")
print(len(tareas))

# Se verifica si un elemento existe dentro de la lista. 
print("\n¿Existe 'programar' en la lista?")
print("programar" in tareas)

# Se verifica cuántas veces aparece un elemento. 
print("\nCantidad de veces que aparece 'ejercicio' :")
print(tareas.count("ejercicio"))

# Se obtiene la posición del elemento "programar".
print("\nPosición del elemento 'programar' :")
print(tareas.index("programar"))

# ¿Qué hace este programa?

# Este programa muestra cómo:
# - Crea una lista. 
# - Acceder a los elementos mediante índices. 
# - Utilizar índice negativos.
# - Conocer el tamaño de una lista. 
# - Verificar si un elemento existe. 
# - Contar cuántas veces aparece un elemento. 
# - Obtener la posición de un elemento. 

