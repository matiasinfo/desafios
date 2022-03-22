numero = int(input("ingrese un numero: "))
if numero % 2 == 0:
    print("el numero es multiplo de 2 ")
    if numero % 3 == 0:
        print("el numero tambien es multiplo de 3")
    if numero % 5 == 0:
        print("el numero tambien es multiplo de 5")
elif numero % 3 == 0:
    print("el numero es multiplo de 3")
    if numero % 5 == 0:
            print("el numero tambien es multiplo de 5")
elif numero % 5 == 0:
    print(" el numero es multiplo de 5")
else:
    print(" el numero ingresado no es multiplo de 2, 3 ni 5")
