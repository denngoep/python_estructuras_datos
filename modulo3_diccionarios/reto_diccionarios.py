# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 3 - Diccionarios
# Reto: Análisis de ventas por región

# 1. Definir ventas_por_region como diccionario anidado
# Cada región contiene las ventas de los cuatro trimestres.

ventas_por_region = {
    "Norte": {
        "Q1": 12000,
        "Q2": 15000,
        "Q3": 17000,
        "Q4": 20000
    },
    "Sur": {
        "Q1": 10000,
        "Q2": 13000,
        "Q3": 14000,
        "Q4": 16000
    },
    "Centro": {
        "Q1": 18000,
        "Q2": 19000,
        "Q3": 21000,
        "Q4": 23000
    },
    "Occidente": {
        "Q1": 9000,
        "Q2": 11000,
        "Q3": 12500,
        "Q4": 14500
    }
}


# 2. Calcular las ventas totales de cada región
# usando items() y sum(values()).

ventas_totales = {}

for region, trimestres in ventas_por_region.items():

    # sum(values()) suma las ventas de Q1, Q2, Q3 y Q4.
    total_region = sum(trimestres.values())

    # Se guarda el total anual de la región.
    ventas_totales[region] = total_region

# 3. Encontrar la región con mayores ventas
# usando max() con key=lambda.

region_mayor_ventas = max(
    ventas_totales.items(),
    key=lambda item: item[1]
)

# 4. Inicializar los totales por trimestre.

totales_por_trimestre = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0
}

# 5. Acumular ventas por trimestre
# utilizando iteración anidada.

for region, trimestres in ventas_por_region.items():

    for trimestre, venta in trimestres.items():

        # Se suma la venta de cada región
        # al trimestre correspondiente.
        totales_por_trimestre[trimestre] += venta


# 6. Calcular el gran total de todas las regiones.

gran_total = sum(ventas_totales.values())

# 7. Generar porcentajes con dict comprehension.

porcentajes = {
    region: (total / gran_total) * 100
    for region, total in ventas_totales.items()
}

# 8. Imprimir reporte ordenado de mayor a menor.

print("REPORTE DE VENTAS POR REGIÓN\n")

# sorted() ordena las regiones según el total de ventas.
# reverse=True permite ordenar de mayor a menor.

for region, total in sorted(
    ventas_totales.items(),
    key=lambda item: item[1],
    reverse=True
):

    print(
        f"Región: {region} | "
        f"Total anual: ${total} | "
        f"Porcentaje: {porcentajes[region]:.2f}%"
    )

# Mostrar la región con mayores ventas.

print("\nREGIÓN CON MAYORES VENTAS")

print(
    f"{region_mayor_ventas[0]} "
    f"con ${region_mayor_ventas[1]}"
)

# Mostrar totales por trimestre.

print("\nTOTALES POR TRIMESTRE")

for trimestre, total in totales_por_trimestre.items():

    print(f"{trimestre}: ${total}")

# Mostrar el gran total.

print("\nGRAN TOTAL DE VENTAS")

print(f"${gran_total}")

# ¿Qué hace este programa?
#
# Este programa analiza las ventas trimestrales de diferentes
# regiones utilizando diccionarios anidados.
#
# Permite:
#
# - Guardar ventas por región y trimestre.
# - Calcular el total anual de cada región.
# - Encontrar la región con mayores ventas.
# - Calcular el total vendido por trimestre.
# - Obtener el gran total de ventas.
# - Calcular el porcentaje que representa cada región.
# - Ordenar el reporte de mayor a menor.
#
# Con este ejercicio se aplican conceptos de:
#
# - Diccionarios.
# - Diccionarios anidados.
# - items().
# - values().
# - sum().
# - max().
# - lambda.
# - Iteración anidada.
# - Dict comprehension.
# - sorted().
