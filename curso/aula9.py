from os import system
system('cls')
print('')

import math
import os 

x = 16
raiz_quad = math.sqrt(x)

print("Riaz quadrarda de",x, "é" ,raiz_quad)
print('')
angulo = 45 
seno = math.sin(angulo)
print("o seno de ",angulo,"é" ,seno)

diretorio = os.getcwd()

print('O diretorio corrente é',diretorio)

lista = [10,20,30]

tam = len(lista)

print("A lista tem tamanho",tam)

soma = sum(lista)

print("A lista ",lista, "tem um somatorio igual a ", soma)