palabra1 = input("ingrese una palabra: ")
cant1 = len(palabra1)
palabra2 = input("ingrese otra palabra diferente: ")
cant2 = len(palabra2)
if cant1 > cant2:
    print("la palabra: {} tiene mayor cantidad de letras".format(palabra1))
elif cant2 > cant1:
    print("la palabra: {} tiene mayor cantidad de letras".format(palabra2))
else:
    print(" la palabras tienen la misma cantidad de letras")