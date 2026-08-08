# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 3 - Diccionarios
# Ejemplo 2: Agregar y modificar elementos


# Se crea un diccionario con información de un estudiante.
estudiante = {
    "nombre": "Dennis",
    "edad": 24,
    "programa": "ADSO"
}

print("Diccionario inicial:")
print(estudiante)

# Se agrega una nueva clave llamada "ciudad".
estudiante["ciudad"] = "Medellín"

print("\nDespués de agregar la ciudad:")
print(estudiante)

# Se modifica el valor de la clave "edad".
estudiante["edad"] = 25

print("\nDespués de modificar la edad:")
print(estudiante)

# También es posible modificar varios valores usando update().
estudiante.update({
    "programa": "Análisis y Desarrollo de Software",
    "estado": "Activo"
})

print("\nDespués de utilizar update():")
print(estudiante)

# ¿Qué hace este programa?
#
# Este programa muestra cómo:
# - Agregar nuevas claves a un diccionario.
# - Modificar el valor de una clave existente.
# - Actualizar uno o varios valores utilizando update().
#
# Los diccionarios permiten agregar y modificar información
# de forma sencilla mediante sus claves.