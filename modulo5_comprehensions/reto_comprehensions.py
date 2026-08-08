# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 5 - Comprehensions
# Reto: Analizador de ventas con las 3 comprehensions

# 1. Definir ventas con 6 productos.
# Cada producto se representa como una tupla:
# (producto, unidades, precio, categoria)

ventas = [
    ("Portátil", 3, 850, "Tecnología"),
    ("Mouse", 20, 25, "Accesorios"),
    ("Teclado", 12, 45, "Accesorios"),
    ("Monitor", 6, 220, "Tecnología"),
    ("Audífonos", 10, 60, "Audio"),
    ("Webcam", 8, 40, "Video")
]


# 2. List comprehension:
# calcular el valor total de cada producto.
#
# valor_total = unidades * precio

valores_totales = [
    unidades * precio
    for producto, unidades, precio, categoria in ventas
]

print("VALORES TOTALES:")
print(valores_totales)


# 3. List comprehension con filtro:
# obtener los nombres de los productos cuyo
# valor total sea mayor a 1000.

productos_destacados = [
    producto
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 1000
]

print("\nPRODUCTOS DESTACADOS:")
print(productos_destacados)


# 4. Dict comprehension:
# crear producto_info mapeando:
# nombre -> {valor, unidades}

producto_info = {
    producto: {
        "valor": unidades * precio,
        "unidades": unidades
    }
    for producto, unidades, precio, categoria in ventas
}

print("\nINFORMACIÓN DE PRODUCTOS:")
print(producto_info)


# 5. Dict comprehension con filtro:
# crear ranking_premium solamente con productos
# cuyo precio sea mayor a 50.

ranking_premium = {
    producto: unidades * precio
    for producto, unidades, precio, categoria in ventas
    if precio > 50
}

# Se ordena el diccionario de mayor a menor
# según el valor total.
ranking_premium = dict(
    sorted(
        ranking_premium.items(),
        key=lambda item: item[1],
        reverse=True
    )
)

print("\nRANKING PREMIUM:")
print(ranking_premium)


# 6. Set comprehension:
# obtener las categorías únicas.

categorias_unicas = {
    categoria
    for producto, unidades, precio, categoria in ventas
}

print("\nCATEGORÍAS ÚNICAS:")
print(categorias_unicas)


# Set comprehension con filtro:
# obtener los productos cuyo precio sea menor
# o igual a 50.

productos_baratos = {
    producto
    for producto, unidades, precio, categoria in ventas
    if precio <= 50
}

print("\nPRODUCTOS BARATOS:")
print(productos_baratos)


# 7. Combinar comprehensions:
# crear un resumen formateado con los productos
# cuyo valor total sea mayor a 1000.

resumen_formateado = {
    producto: (
        f"{unidades} unidades x ${precio} = "
        f"${unidades * precio}"
    )
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 1000
}

print("\nRESUMEN FORMATEADO:")

for producto, resumen in resumen_formateado.items():
    print(f"{producto}: {resumen}")


# 8. Calcular el gran total utilizando sum().

gran_total = sum(
    unidades * precio
    for producto, unidades, precio, categoria in ventas
)

print("\nGRAN TOTAL DE VENTAS:")
print(f"${gran_total}")



# ¿Qué hace este programa?
#
# Este programa analiza un conjunto de ventas utilizando
# List Comprehension, Dict Comprehension y Set Comprehension.
#
# Permite:
#
# - Calcular el valor total de cada producto.
# - Filtrar productos con ventas superiores a 1000.
# - Crear un diccionario con información de cada producto.
# - Crear un ranking de productos premium.
# - Obtener las categorías únicas.
# - Identificar productos baratos.
# - Crear un resumen formateado de productos destacados.
# - Calcular el gran total de todas las ventas.
#
# Con este ejercicio se aplican conceptos de:
#
# - List Comprehension.
# - List Comprehension con filtros.
# - Dict Comprehension.
# - Dict Comprehension con filtros.
# - Set Comprehension.
# - Set Comprehension con filtros.
# - sorted().
# - lambda.
# - sum().