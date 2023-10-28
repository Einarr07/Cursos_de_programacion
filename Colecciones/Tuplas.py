# Tuplas

# Las tuplas son inmutables

# Todo tipo de busqueda en las tuplas esta permitido

tupla = (4,5,6,2,3,6,9,8,52,["Hernesto", "Jaime"],6,65,6.46,)

print(tupla[1:])

print(tupla[4])

print("Hernesto" in tupla)

print(tupla.index(65))

# para transformar una tupla en una lista utilizamos list()

lista = list(tupla)
print(lista)

