# Pilas (Con listas)
# El ultimo en entrar es el primero en salir
# EJ: Estante de libros

pila = [1,2,3]

# Agregando elementos por el final
pila.append(4)
pila.append(5)

print(pila)
# Sacando elementos por el final

ultimo = pila.pop()
print(f"Se retiro el elemento {ultimo}")

print(pila)