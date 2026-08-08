# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 3 - Diccionarios
# Ejemplo 5: Diccionarios anidados


# Se crea un diccionario donde cada estudiante
# tiene su propia información.
estudiantes = {
    "1001": {
        "nombre": "Dennis",
        "edad": 24,
        "programa": "ADSO"
    },
    "1002": {
        "nombre": "María",
        "edad": 24,
        "programa": "Contabilidad"
    },
    "1003": {
        "nombre": "Carlos",
        "edad": 28,
        "programa": "Enfermería"
    }
}

print("Información de los estudiantes:\n")

# Se recorren los estudiantes.
for documento, datos in estudiantes.items():

    print(f"Documento: {documento}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Programa: {datos['programa']}")
    print("--------------------------")

# ¿Qué hace este programa?
#
# Este programa muestra cómo trabajar con
# diccionarios anidados.
#
# Cada estudiante está identificado por un documento
# y su información se almacena en otro diccionario.
#
# Luego se recorre el diccionario principal utilizando
# items() para acceder tanto a la clave como al valor.