# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 4 - Conjuntos
# Ejemplo 4: Recorrer conjuntos

# Se crea un conjunto con nombres de ciudades.
ciudades = {"Medellín", "Bogotá", "Cali", "Barranquilla"}

print("Ciudades registradas:\n")

# Se recorre el conjunto utilizando un ciclo for.
for ciudad in ciudades:

    print(ciudad)

print("\nVerificando si una ciudad pertenece al conjunto:")

# Se verifica si Medellín pertenece al conjunto.
if "Medellín" in ciudades:

    print("Medellín sí pertenece al conjunto.")

else:

    print("Medellín no pertenece al conjunto.")

# ¿Qué hace este programa?
#
# Este programa muestra cómo recorrer un conjunto
# utilizando un ciclo for.
#
# También verifica si un elemento pertenece
# al conjunto utilizando el operador in.
#
# Los conjuntos no poseen índices, por lo que
# únicamente pueden recorrerse elemento por elemento.