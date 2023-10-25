print("Bienvenido, esta es una simulación de una calculadora básica\n"
      "Para hacer cualquierda de las siguientes operaciones debes ingresar la letra correspondiente\n"
      "S-s = Suma\nR-r = Resta\nP-p o M-m = Multiplicación\nD-d = División")

opcion = input("Ingresa la letra de la operación que quieras realizar: ").upper()

# SUMA
if opcion == "S":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
    # RESTA
elif opcion == "R":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
    # MULTIPLICACIÓN
elif opcion == "P" or opcion == "M":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
    # DIVISIÓN
elif opcion == "D":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
    # No ingreso una opción correcta
else:
    print("No ingresaste una opción correcta, vuelve a intentar")