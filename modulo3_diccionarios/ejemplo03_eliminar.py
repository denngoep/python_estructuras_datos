# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 3 - Diccionarios
# Ejemplo 3: Eliminar elementos de un diccionario

# Se crea un diccionario con información de un estudiante.
estudiante = {
    "nombre": "Dennis",
    "edad": 24,
    "programa": "ADSO",
    "ciudad": "Medellín"
}

print("Diccionario inicial:")
print(estudiante)

# pop() elimina una clave y devuelve su valor.
ciudad = estudiante.pop("ciudad")

print("\nValor eliminado:")
print(ciudad)

print("\nDiccionario después de pop():")
print(estudiante)

# del elimina una clave específica.
del estudiante["edad"]

print("\nDiccionario después de del:")
print(estudiante)

# clear() elimina todos los elementos del diccionario.
estudiante.clear()

print("\nDiccionario después de clear():")
print(estudiante)

# ¿Qué hace este programa?
#
# Este programa muestra diferentes formas de eliminar
# información de un diccionario.
#
# pop() -> Elimina una clave y devuelve su valor.
# del -> Elimina una clave específica.
# clear() -> Elimina todos los elementos del diccionario.