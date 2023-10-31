# Diccionarios

diccionario = {
    "azul": "blue",
    "rojo": "red",
    "verde": "green"
}

diccionario2 = {
    "Alejandro": [22,1.73],
    "Pedro": [28,1.60],
    "María": [27,1.63]
}

# AGG y modificar
diccionario["amarrillo"] = "yellow"

# Borrar
del(diccionario["verde"])

print(diccionario2)

print("--------------------------")
print("\nDiccionario parte 2")

equipo = {
    11:"Martin Jimenez",
    22:"Ener Valencia",
    13:"Jamie Calderon",
    4:"Mario Castañeda"
}

print(equipo.get(6, "No existe un jugador con ese número"))
print(equipo.keys())
print(len(equipo))
