num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))

if num1%2 == 0 and num2%2 == 0:
    print("Ambos números son pares")
elif num1%2 == 0:
    print(f"Solo el {num1} es par")
elif num2%2 == 0:
    print(f"Solo el {num2} es par")
else:
    print("Ningun número es par")