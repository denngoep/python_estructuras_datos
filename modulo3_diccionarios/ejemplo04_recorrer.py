# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 3 - Diccionarios
# Ejemplo 4: Recorrer diccionarios

# Se crea un diccionario con información de un estudiante.
estudiante = {
    "nombre": "Dennis",
    "edad": 24,
    "programa": "ADSO",
    "ciudad": "Medellín"
}

print("Recorrer las claves:")

# keys() devuelve todas las claves del diccionario.
for clave in estudiante.keys():
    print(clave)

print("\nRecorrer los valores:")

# values() devuelve todos los valores del diccionario.
for valor in estudiante.values():
    print(valor)

print("\nRecorrer claves y valores:")

# items() devuelve la clave y el valor al mismo tiempo.
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

# ¿Qué hace este programa?
#
# Este programa muestra tres formas de recorrer
# un diccionario.
#
# keys() -> Recorre únicamente las claves.
# values() -> Recorre únicamente los valores.
# items() -> Recorre simultáneamente la clave y el valor.
#
# El método items() es el más utilizado cuando se necesita
# trabajar con toda la información del diccionario.