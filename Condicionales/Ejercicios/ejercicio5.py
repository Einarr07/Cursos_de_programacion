print("Este es un simulador de un cajero automatico tu valor inicial es de $1000 y puedes hacer las siguientes acciones:")
print("1.- Ingresar dinero en la cuenta")
print("2.- Retirar dinero de la cuenta")
print("3.- Mostrar dinero disponible")
print("4.- Salir")

monto_inicial = 1000

try:
    opcion = int(input("Ingresa la opción que de deseas realizar: "))
    if opcion == 1:
        try:
            print("NOTA: El minimo a ingresar es de 0.10ctvs")
            monto_ingresado = float(input("¿Cuánto dinero deseas ingresar?: "))
            if (monto_ingresado >= 0.1):
                monto_inicial += monto_ingresado
                print(f"El monto total de tu cuenta después de la transacción es: ${monto_inicial}")
            else:
                print("No puedes ingresar valores negativos.")
        except ValueError:
            print("No puedes ingresar letras, por favor ingresa un número valido.")
    elif opcion == 2:
        try:
            print("NOTA: El minimo a retirar es de $1.00ctvs")
            monto_a_retirar = float(input("¿Cuánto dinero deseas retirar?: "))
            if (monto_a_retirar >= 1.00 and monto_a_retirar <= monto_inicial):
                monto_inicial -= monto_a_retirar
                print(f"El monto total de tu cuenta después de la transacción es: ${monto_inicial}")
            else:
                print(f"Su saldo es de ${monto_inicial}, no puede retirar una cantidad mayor a ${monto_inicial}")
        except ValueError:
            print("No puedes ingresar letras, por favor ingresa un número valido.")
    elif opcion == 3:
        print(f"El monto que tienes en tu cuenta es de: ${monto_inicial}")
    elif opcion == 4:
        print("Gracias vuelva pronto.")
    else:
        print(f"La opción que ingresaste '{opcion}', no es valida.")
except ValueError:
    print("No puedes ingresar letras, por favor ingresa un número valido.")