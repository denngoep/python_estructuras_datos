# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 2 - Tuplas
# Ejemplo 4: Tuplas anidadas

# Se crea una tupla que contiene otras tuplas. 
estudiantes = (
    ("Dennis", 24, "ADSO"),
    ("Dayana", 30, "Contabilidad"),
    ("Marcela", 25, "Enfermería"),
)

print("Información de los estudiantes:\n")

# Se recorre la tupla principal.
for estudiante in estudiantes:

    # Se muestra los datos de cada estudiante. 
    print(f"Nombre: {estudiante[0]}")
    print(f"Edad: {estudiante[1]}")
    print(f"Programa: {estudiante[2]}")
    print("------------------------")

# ¿Qué hace este programa?

# Este programa muestra cómo trabajar con tuplas anidadas.

# Cada estudiantes está representado por una tupla y todas
# las tuplas se almacenan dentro de una tupla principal. 

# Luego se utiliza un ciclo for para recorrer cada registro. 