num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercer número entero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número máyor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número máyor es: {num2}")
elif num3 >= num2 and num3 >= num1:
    print(f"El número máyor es: {num3}")

