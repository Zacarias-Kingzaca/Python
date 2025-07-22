from os import system
from utilidadescv import moeda
system("cls")
print()

n = float(input("Digita o preço: kzs:"))
moeda.resumo(n, 35, 22)