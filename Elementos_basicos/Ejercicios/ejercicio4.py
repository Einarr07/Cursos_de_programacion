import math

print("Este es un programa para calcular el area y la longitud de un circulo "
      "a trabes de su radio")

radio = float(input("Por favor ingresa el radio del circulo: "))

# Operación
area = math.pi * radio**2

longitud = 2 * math.pi * radio

print(f"El area del circulo es: {area:.2f}\ny su longitud es: {longitud:.2f}")
