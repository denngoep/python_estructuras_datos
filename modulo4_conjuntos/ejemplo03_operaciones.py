# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 4 - Conjuntos
# Ejemplo 3: Operaciones entre conjuntos

# Se crean dos conjuntos.
grupo_a = {"Python", "Java", "C#", "PHP"}
grupo_b = {"Python", "JavaScript", "PHP", "Kotlin"}

print("Grupo A:")
print(grupo_a)

print("\nGrupo B:")
print(grupo_b)

# Unión de conjuntos.
print("\nUnión:")
print(grupo_a | grupo_b)

# Intersección de conjuntos.
print("\nIntersección:")
print(grupo_a & grupo_b)

# Diferencia entre conjuntos.
print("\nDiferencia A - B:")
print(grupo_a - grupo_b)

print("\nDiferencia B - A:")
print(grupo_b - grupo_a)

# Diferencia simétrica.
print("\nDiferencia simétrica:")
print(grupo_a ^ grupo_b)

# ¿Qué hace este programa?
#
# Este programa muestra las principales operaciones
# entre conjuntos.
#
# | -> Unión.
# & -> Intersección.
# - -> Diferencia.
# ^ -> Diferencia simétrica.
#
# Estas operaciones permiten comparar conjuntos
# de forma rápida y eficiente.