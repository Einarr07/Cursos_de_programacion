# Conjuntos

# Son grupo de elementos desordenados donde no puede haber duplicados

# Para crear un conjunto vacio utilizamos la funcion set()
conjunto = set()
conjunto = {23,546,54,8, "María", "Pedrito"}

# Para agregar un conjunto
conjunto.add(8)

# Para eliminar un elemento
conjunto.discard(54)

# Para borrar todo el conjunto utilizamos la función clear()

print(conjunto)

print("----------------------")
print("\nConjuntos parte 2")

a = {1,2,3}
b = {3,4,5,6}

# Para realizar la union de dos conjuntos utilizamos |
c = a | b
print(c)

# Para hacer la intersección entre dos conjuntos utilizamos &
d = a & b
print(d)

# Para saber la diferencia entre dos conjuntos utilizamos -
# En este caso vemos elementos que estan en a y no en b
e = a - b
print(e)

# Para saber la diferencia simetrica utilimamos ^
# NOTA: La diferencia siemetrica son elementos que estan en a y en b pero NO en ambos
f = a ^ b
print(f)

# Para determinar si un conjunto es subconjunto de otro
g = {1,2,3,4,5,6}
print(a.issubset(g))

# Para determinar si el conjunto tienes todos los elementos de otro
h = {1,2,3,4,5,6}
print(h.issuperset(a))

# Para saber si NO comparte algun elemento en comun
print(a.isdisjoint(b))

# Conjuntos inmutables
i = frozenset({97,23,43,54})
print(i)