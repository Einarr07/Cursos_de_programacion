# Listas primera parte
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", [1,2,3,4,5], True, False, 35.0, 65.34]

# Para mostrar los elementos de la lista se empieza desde el 0
print(lista[0])

# Para mostrar el ultimo elemento hacia adelante se empieza por el -1
print(lista[-3])

# Con esto definimos un rango para mostrar tambien se puede colocar [:5]
print(lista[0:4])

# Para contar los elementos que existe en la lista podemos utilizar la función len
print(len(lista))

# Lista segunda parte
print("--------------------------")
print("\nLista segunda parte")

lista2 = [1,2,4,5,6]

# Para agregar elementos a una lista utilizamos la función append()
lista2.append(7)

# Para insertar un elemento especifico en la lista utilizamos insert()
# y se le pasan 2 valores primero el indice y luego el valor
lista2.insert(2,3)

# Si queremos agregar varios elementos a la lista utilizamos extend(
lista2.extend([8,9,10])

print(lista2)

# Buscar un elemento en la lista
print(3 in lista2)

# En que indice se encuentra el elemento
print(f"El elemento 7 se encuentra en la posición: {lista2.index(7)} de la lista")

print("---------------------")
print("\nLista 3ra parte")

lista3 = ["Juan", "Mathias", "Marco", "Hermes", "Juan", "María", "Pepe"]
lista4 = [87,9,5,654,213,231,85,68,657,46,3121,6,574,3,4,687,5,]
# Para contar cuantos elementos exactos existen en la lista utilizamos la función count()
print(lista3.count("Juan"))

# Para eliminar elementos de la lista utilizamos la función pop() y le pasamos el INDICE
# Si no ponemos nada pop elimina el ultimo indice de la lista
lista3.pop(2)
print(lista3)

# Para eliminar un elemento por su valor utilizamos la función remove()
lista3.remove("María")
print(lista3)

# Para invertir los valores de la lista utilizamos la función reverse()
lista3.reverse()
print(lista3)

# Para que la lista quede vacia utilizamos la función clear()
lista3.clear()
print(lista3)

# Para ordenar los elementos en una lista utilizamos la función sort()
lista4.sort()
print(lista4)