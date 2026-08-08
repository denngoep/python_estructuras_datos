# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 3 - Diccionarios
# Ejemplo 1: Creación y acceso a diccionarios

# Se crea un diccionario con información de un estudiante.
estudiante = {
    "nombre": "Dennis",
    "edad": 24,
    "programa": "ADSO"
}

# Se muestra el diccionario completo.
print("Diccionario completo:")
print(estudiante)

# Se accede al valor asociado a la clave "nombre".
print("\nNombre:")
print(estudiante["nombre"])

# Se accede al valor asociado a la clave "edad".
print("\nEdad:")
print(estudiante["edad"])

# Se accede al valor asociado a la clave "programa".
print("\nPrograma:")
print(estudiante["programa"])

# Se utiliza get() para obtener un valor.
print("\nPrograma usando get():")
print(estudiante.get("programa"))

# Se muestra la cantidad de elementos del diccionario.
print("\nCantidad de elementos:")
print(len(estudiante))

# ¿Qué hace este programa?

# Este programa muestra cómo:
# - Crear un diccionario.
# - Guardar información mediante pares clave: valor.
# - Acceder a los valores utilizando sus claves.
# - Utilizar el método get().
# - Obtener la cantidad de elementos con len().
#
# Los diccionarios permiten organizar información
# utilizando claves descriptivas en lugar de índices