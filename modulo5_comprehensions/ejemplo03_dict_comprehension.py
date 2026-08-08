# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 5 - Comprehensions
# Ejemplo 3: Dict Comprehension

# Se crea una lista con los nombres de varios estudiantes.
estudiantes = ["Dennis", "María", "Carlos", "Laura"]

print("Lista de estudiantes:")
print(estudiantes)

# Se crea un diccionario donde la clave es el nombre
# y el valor corresponde a la cantidad de letras.
cantidad_letras = {
    estudiante: len(estudiante)
    for estudiante in estudiantes
}

print("\nCantidad de letras por estudiante:")
print(cantidad_letras)

# ¿Qué hace este programa?
#
# Este programa muestra cómo crear un diccionario
# utilizando Dict Comprehension.
#
# La clave corresponde al nombre del estudiante y
# el valor corresponde a la cantidad de letras
# que tiene su nombre.