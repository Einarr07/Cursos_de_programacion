
edad = int(input("Ingresa tu edad: "))

# tambien se puede colocar 0 < edad < 110
# con esto decimos que la edad debe estar dentro de un rango que es entre 0 y 110
if edad > 0 and edad < 110:
    print("Edad correcta")
    if edad >= 18:
        print("Eres mayot de edad, vienvenido al estres de ser adulto")
else:
    print("Enserio?")