# Ejercicio Nº2

nombres = ["Ana", "Carlos", "Elena", "Carlos", "Fernando", "Elena", "Diana", "Gustavo", "Laura", "Carlos"]

nombres2 = ["Luis", "María", "Pedro", "María", "Javier", "Pedro", "Luis", "Lucía", "Elena", "Diana"]


# Lo transformo en un conjunto para que no existan repeticiones
nombres = set(nombres)

nombres2 = set(nombres2)

# Todos los elementos que aparecen en las dos listas
lista_nombres = list(nombres | nombres2)
print(f"Los elementos en las 2 listas son: {lista_nombres}")

# Elementos que aparecen en la primera lista pero no en la segunda
primera_lista = list(nombres - nombres2)
print(f"Los elementos que existen solo en la primera lista son: {primera_lista}")

# Elementos que aparecen en la segunda lista pero no en la primera
segunda_lista = list(nombres2 - nombres)
print(f"Los elementos que existen solo en la segunda lista son: {segunda_lista}")

# Elementos que existen en las dos listas
interseccion = list(nombres & nombres2)
print(f"Los elementos comunes entre las dos listas son: {interseccion}")