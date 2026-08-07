# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 1 - Listas
# Ejemplo 6: Recorrer listas

# Se crea una lista con nombres de estudiantes. 
estudiantes = ["Ana", "Carlos", "María", "Luis", "Sofía"]

print("Lista de estudiantes:")
print(estudiantes)

print("\nRecorrido utilizando un ciclo for:")

# Se recorrre la lista mostrando cada elemento. 
for estudiante in estudiantes:
    print(estudiante)

    print("\nRecorrido utilizando índices:")

# Se recorre la lista utilizando los índices.
for i in range(len(estudiantes)):
    print(f"Posición {i}: {estudiantes[i]}")

# ¿Qué hace este programa?

# Este programa muestra dos formas de recorres una lista:

# 1. Utilizando un cilo for directamente sobre los elementos. 
# 2. Utilizando los índices con rage() y len()