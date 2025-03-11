from os import system
from datetime import date
system("cls")
print()
totmaior = 0
totmenor = 0
atual = date.today().year
for i in range(1, 8):
    nasc = int(input("Em que ano a {}º pessoa nasceu? ".format(i)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Tevemos o total de {} pessoas maiores de idade".format(totmaior))
print("Tevemos o total de {} pessoas menores de idade".format(totmenor))
 

