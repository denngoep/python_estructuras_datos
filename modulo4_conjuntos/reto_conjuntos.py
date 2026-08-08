# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 4 - Conjuntos
# Reto: Tiendas y recomendaciones de películas

# 1. Definir tienda_centro, tienda_norte y tienda_sur
# como conjuntos de productos.

tienda_centro = {
    "Arroz",
    "Leche",
    "Pan",
    "Huevos",
    "Café"
}

tienda_norte = {
    "Leche",
    "Pan",
    "Huevos",
    "Azúcar",
    "Chocolate"
}

tienda_sur = {
    "Arroz",
    "Leche",
    "Pan",
    "Aceite",
    "Galletas"
}

# 2. Calcular catálogo completo con union().

catalogo_completo = tienda_centro.union(
    tienda_norte,
    tienda_sur
)

productos_comunes = tienda_centro.intersection(
    tienda_norte,
    tienda_sur
)

# 3. Calcular productos exclusivos de cada tienda.
#
# Primero se unen las otras dos tiendas y luego
# se utiliza difference().

exclusivos_centro = tienda_centro.difference(
    tienda_norte.union(tienda_sur)
)

exclusivos_norte = tienda_norte.difference(
    tienda_centro.union(tienda_sur)
)

exclusivos_sur = tienda_sur.difference(
    tienda_centro.union(tienda_norte)
)

# Verificar si existen solapamientos entre las tiendas
# utilizando isdisjoint().
#
# isdisjoint() devuelve True si los conjuntos NO
# tienen elementos en común.

centro_norte_sin_comunes = tienda_centro.isdisjoint(
    tienda_norte
)

centro_sur_sin_comunes = tienda_centro.isdisjoint(
    tienda_sur
)

norte_sur_sin_comunes = tienda_norte.isdisjoint(
    tienda_sur
)

# 4. Definir tres usuarios como conjuntos de
# géneros cinematográficos.

usuario1 = {
    "Acción",
    "Ciencia ficción",
    "Drama",
    "Comedia"
}

usuario2 = {
    "Acción",
    "Drama",
    "Terror",
    "Suspenso"
}

usuario3 = {
    "Drama",
    "Comedia",
    "Animación",
    "Ciencia ficción"
}

# 5. Usar operadores matemáticos de conjuntos.


# & obtiene los géneros comunes entre los tres usuarios.

generos_comunes = usuario1 & usuario2 & usuario3


# | obtiene el universo de géneros preferidos.

universo_generos = usuario1 | usuario2 | usuario3


# - obtiene géneros exclusivos del usuario 1
# respecto a los otros usuarios.

exclusivos_usuario1 = usuario1 - (usuario2 | usuario3)


# ^ obtiene la diferencia simétrica.
#
# Devuelve elementos que se encuentran en uno de los
# conjuntos pero no simultáneamente en ambos.

diferencia_usuario1_usuario2 = usuario1 ^ usuario2


# 6. Utilizar <= para verificar subconjuntos.
#
# Se crea un conjunto con géneros para verificar
# si todos pertenecen al usuario 1.

preferencias_basicas = {
    "Acción",
    "Drama"
}

es_subconjunto = preferencias_basicas <= usuario1

# RESUMEN FINAL

print("===== ANÁLISIS DE TIENDAS =====")

print("\nCatálogo completo:")
print(catalogo_completo)

print("\nProductos comunes en las tres tiendas:")
print(productos_comunes)

print("\nProductos exclusivos de Tienda Centro:")
print(exclusivos_centro)

print("\nProductos exclusivos de Tienda Norte:")
print(exclusivos_norte)

print("\nProductos exclusivos de Tienda Sur:")
print(exclusivos_sur)


print("\n¿Centro y Norte no tienen productos en común?")
print(centro_norte_sin_comunes)

print("\n¿Centro y Sur no tienen productos en común?")
print(centro_sur_sin_comunes)

print("\n¿Norte y Sur no tienen productos en común?")
print(norte_sur_sin_comunes)


print("\n===== RECOMENDACIONES DE PELÍCULAS =====")

print("\nGéneros comunes entre los tres usuarios:")
print(generos_comunes)

print("\nUniverso de géneros:")
print(universo_generos)

print("\nGéneros exclusivos del usuario 1:")
print(exclusivos_usuario1)

print("\nDiferencia entre usuario 1 y usuario 2:")
print(diferencia_usuario1_usuario2)

print("\n¿Las preferencias básicas son subconjunto del usuario 1?")
print(es_subconjunto)


# ¿Qué hace este programa?
#
# Este programa utiliza conjuntos para analizar productos
# disponibles en tres tiendas y preferencias de películas.
#
# Permite:
#
# - Unir catálogos de varias tiendas.
# - Encontrar productos comunes.
# - Identificar productos exclusivos.
# - Verificar si dos conjuntos no tienen elementos comunes.
# - Comparar preferencias de géneros cinematográficos.
# - Obtener géneros comunes entre usuarios.
# - Crear un universo de preferencias.
# - Encontrar géneros exclusivos.
# - Calcular diferencias simétricas.
# - Verificar si un conjunto es subconjunto de otro.
#
# Con este ejercicio se aplican conceptos de:
#
# - Conjuntos.
# - union().
# - intersection().
# - difference().
# - isdisjoint().
# - Operador &.
# - Operador |.
# - Operador -.
# - Operador ^.
# - Operador <=.