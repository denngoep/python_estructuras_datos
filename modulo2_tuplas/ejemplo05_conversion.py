# Autor: Dennis González
# Programa: ADSO - SENA
# Actividad: GA1 220501093-04 AA1 EV03
# Módulo 2 - Tuplas
# Ejemplo 5: Conversión entre listas y tuplas


# Se crea una lista.
frutas_lista = ["Manzana", "Banano", "Pera"]

print("Lista orgininal:")
print(frutas_lista)

# Se convierte la lista en una tupla.
frutas_tuplas = tuple(frutas_lista)

print("\nLista convertida en tupla:")
print(frutas_tuplas)

# Se convierte nuevamente la tupla en una lista. 
frutas_lista_nueva = list(frutas_tuplas)


print("\nTupla convertida nuevamente en lista:")
print(frutas_lista_nueva)

# Se agrega un nuevo elemento a la lista. 
frutas_lista_nueva.append("Uva")

print("\nLista después de agregar un nuevo elemento:")
print(frutas_lista_nueva)


# ¿Qué hace este programa?

# Este programa muestra cómo convertir una lista en una
# tupla utilizando tuple() y cómo convertir una tupla en una 
# lista utilizando list()

# Esto resulta útil cuando se necesita modificar una tupla,
# ya que primero debe convertirse en lista, realizar los
# cambios y, si es necesario, volver a convertila en tupla. 

