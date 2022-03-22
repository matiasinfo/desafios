cadena = input("ingrese una palabra: ")
cant = 0
for car in cadena:
    if car == "a" or car == "A":
        cant += 1
if cant > 0:
    print("la cantidad de letras A que contiene la palabra es: {}".format(cant))