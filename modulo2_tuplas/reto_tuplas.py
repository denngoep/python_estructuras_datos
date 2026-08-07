# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 2 - Tuplas
# Reto: Sistema de películas

# 1. Definir catalogo como tupla de subtuplas
# Cada película contiene:
# (titulo, director, año, puntuacion)

catalogo = (
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("Interstellar", "Christopher Nolan", 2014, 8.7),
    ("Parasite", "Bong Joon-ho", 2019, 8.5),
    ("The Godfather", "Francis Ford Coppola", 1972, 9.2)
)


# 2. Recorrer catalogo con for desempaquetando los cuatro campos

print("CATÁLOGO DE PELÍCULAS\n")

for titulo, director, anio, puntuacion in catalogo:

    print(f"Título: {titulo}")
    print(f"Director: {director}")
    print(f"Año: {anio}")
    print(f"Puntuación: {puntuacion}")
    print("----------------------------")


# 3. Usar operador * para separar primera película del resto

primera_pelicula, *resto_peliculas = catalogo

print("\nPRIMERA PELÍCULA:")
print(primera_pelicula)

print("\nRESTO DE PELÍCULAS:")
print(resto_peliculas)


# 4. Definir buscar_por_director(director)

def buscar_por_director(director):

    # Se crea una tupla vacía para guardar coincidencias.
    coincidencias = ()

    # Se recorren todas las películas del catálogo.
    for pelicula in catalogo:

        # Se verifica si el director de la película
        # coincide con el director recibido.
        if pelicula[1] == director:

            # Se agrega la película a la tupla de coincidencias.
            coincidencias += (pelicula,)

    # Se devuelve una tupla con las películas encontradas.
    return coincidencias


# 5. Definir obtener_estadisticas(peliculas)

def obtener_estadisticas(peliculas):

    # Se crea una tupla con las puntuaciones.
    puntuaciones = ()

    # Se recorren las películas recibidas.
    for pelicula in peliculas:

        # Se agrega la puntuación de cada película.
        puntuaciones += (pelicula[3],)

    # Se obtiene la puntuación mínima.
    minima = min(puntuaciones)

    # Se obtiene la puntuación máxima.
    maxima = max(puntuaciones)

    # Se calcula el promedio.
    promedio = sum(puntuaciones) / len(puntuaciones)

    # Se retorna una tupla con los tres resultados.
    return (minima, maxima, promedio)


# 6. Llamar a buscar_por_director e imprimir coincidencias

peliculas_nolan = buscar_por_director("Christopher Nolan")

print("\nPELÍCULAS DE CHRISTOPHER NOLAN:")

for pelicula in peliculas_nolan:
    print(pelicula)


# 7. Desempaquetar retorno de obtener_estadisticas

minima, maxima, promedio = obtener_estadisticas(catalogo)


# 8. Imprimir mínima, máxima y promedio

print("\nESTADÍSTICAS DE PUNTUACIÓN")

print(f"Puntuación mínima: {minima}")
print(f"Puntuación máxima: {maxima}")
print(f"Puntuación promedio: {promedio:.2f}")


# ============================================================
# ¿Qué hace este programa?
#
# Este programa crea un catálogo de películas utilizando
# una tupla de tuplas.
#
# Permite:
# - Guardar información de películas de forma inmutable.
# - Desempaquetar los datos de cada película.
# - Separar la primera película del resto usando *.
# - Buscar películas por director.
# - Obtener estadísticas de puntuación.
# - Calcular puntuación mínima, máxima y promedio.
#
# Con este ejercicio se aplican conceptos de:
#
# - Tuplas.
# - Tuplas anidadas.
# - Desempaquetado.
# - Operador *.
# - Ciclos for.
# - Funciones.
# - min().
# - max().
# - sum().
# - len().