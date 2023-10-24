# Escriba la sigueinte expresion en forma algoritmica
"""
a al cubo por (b al cuadrado menos 2ac) dividido  para 2b

"""

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

resultado = (a**3 * (b**2 - 2*a*c)) / (2*b)

print(f"El resultado de la expresión algoritmica es: {resultado}")