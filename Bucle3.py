import os
os.system("cls")

estado = True

while estado :
    TABLA = int(input("Digite tabla de multiplicar: "))

    if TABLA < 1 :
        estado = True
        print("::: La tabla de multiplicar debe ser positiva :::")
    else :
        estado = False

Li = int(input("Ingrese límite inferior: "))
Ls = int(input("Ingrese límite superior: "))

i = Li
while i <= Ls :
    print (TABLA, " x ", i, " = ", TABLA * i)
    i = i + 1