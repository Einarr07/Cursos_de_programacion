precio = float(input("Ingresa el precio de tu producto: "))

# Operación
descuento = (precio*15)/100
precio_final = precio - descuento

print(f"El precio final de tu producto con un 15% de descuento es: ${precio_final:.2f}")