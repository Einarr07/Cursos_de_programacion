a = float(input("Ingresar el valor de a: "))
b = float(input("Ingresar el valor de b: "))

# De una forma simplificada es: a , b = b , a
x = a
a = b
b = x

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
