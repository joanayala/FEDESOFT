#Tabla de multiplicar básica con serie del 1 al 10
#Con número constante
#TABLA = 4

import os

os.system("cls")


TABLA = int(input("Digite tabla de multiplicar: "))
i = 1
while i <= 10 :
    print (TABLA, " x ", i, " = ", TABLA * i)
    i = i + 1
