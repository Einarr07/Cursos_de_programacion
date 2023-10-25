caracter = input("Ingresa solo un caracter: ").lower()

if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
    print("Esta es una vocal")
else:
    print(f"{caracter} no es una vocal")
