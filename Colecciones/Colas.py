# Colas
# El primero en entrar es el primero en salir
# EJ: Personas en un banco

colaBanco = ["Martin", "Juan", "Jose", "Miguel"]

# Agregamos elementos al final de la cola
colaBanco.append("Karla")
colaBanco.append("Patricia")
print(f"Total de personas en la cola:\n{colaBanco}")

# Sacamos elementos por el principio
personaAtendida = colaBanco.pop(0)
print(f"Atendiendo a: {personaAtendida}")

print(f"Personas que quedan en la cola: {colaBanco}")


