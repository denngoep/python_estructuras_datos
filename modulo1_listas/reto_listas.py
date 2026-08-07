# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 1 - Listas
# Reto: Gestión de inventario

# 1. Definir inventario con tres productos
# Cada producto se representa con:
# [nombre, cantidad, precio]

inventario = [
    ["Arroz", 20, 3500],
    ["Leche", 15, 4200],
    ["Pan", 30, 2000]
]

# 2. Función para actualizar el precio de un producto

def actualizar_precio(producto, nuevo_precio):

    # Se recorre cada producto almacenado en el inventario.
    for item in inventario:

        # Se compara el nombre del producto recibido
        # con el nombre almacenado en el inventario.
        if item[0] == producto:

            # Se actualiza el precio ubicado en la posición 2.
            item[2] = nuevo_precio

            print(f"Precio de {producto} actualizado a ${nuevo_precio}")

            # Se termina la función porque el producto ya fue encontrado.
            return

    # Este mensaje se muestra si el producto no existe.
    print(f"El producto {producto} no se encuentra en el inventario.")


# 3. Función para registrar una venta

def registrar_venta(producto, cantidad):

    # Se recorre el inventario buscando el producto.
    for item in inventario:

        # Se verifica si el producto existe.
        if item[0] == producto:

            # Se verifica si existe suficiente stock.
            if item[1] >= cantidad:

                # Se descuenta del stock la cantidad vendida.
                item[1] -= cantidad

                print(
                    f"Venta registrada: {cantidad} unidades de {producto}"
                )

            else:

                # Se muestra un mensaje si no hay suficiente cantidad.
                print(
                    f"Stock insuficiente para vender "
                    f"{cantidad} unidades de {producto}"
                )

            # Se termina la función porque el producto ya fue encontrado.
            return

    # Se muestra si el producto no fue encontrado.
    print(f"El producto {producto} no se encuentra en el inventario.")


# 4. Función para añadir un producto

def anadir_producto(producto, cantidad, precio):

    # Se recorre el inventario para comprobar
    # si el producto ya existe.
    for item in inventario:

        if item[0] == producto:

            # Si existe, se aumenta la cantidad disponible.
            item[1] += cantidad

            print(
                f"Se agregaron {cantidad} unidades al producto {producto}"
            )

            return

    # Si el producto no existe, se crea una nueva sublista.
    inventario.append([producto, cantidad, precio])

    print(f"Producto nuevo agregado: {producto}")


# 5. Función para mostrar el inventario

def mostrar_inventario():

    print("\nINVENTARIO FINAL")

    # Se recorre cada producto del inventario.
    for item in inventario:

        # Se muestra nombre, cantidad y precio.
        print(
            f"Producto: {item[0]} | "
            f"Cantidad: {item[1]} | "
            f"Precio: ${item[2]}"
        )


# Llamar a actualizar_precio con el segundo producto

actualizar_precio("Leche", 4500)

# Llamar a registrar_venta con el primer producto

registrar_venta("Arroz", 5)

# Llamar a anadir_producto con un producto nuevo

anadir_producto("Huevos", 24, 700)

# Mostrar el inventario final

mostrar_inventario()


# ¿Qué hace este programa?

# Este programa utiliza listas anidadas para administrar
# un inventario de productos.

# Permite:
# - Guardar nombre, cantidad y precio de cada producto.
# - Actualizar el precio de un producto.
# - Registrar una venta y disminuir el stock.
# - Verificar que exista suficiente stock antes de vender.
# - Añadir un producto nuevo.
# - Aumentar el stock si el producto ya existe.
# - Mostrar el estado final del inventario.

# Con este ejercicio se aplican conceptos de:

# - Listas.
# - Listas anidadas.
# - Índices.
# - Ciclos for.
# - Condicionales.
# - Funciones.
# - append().