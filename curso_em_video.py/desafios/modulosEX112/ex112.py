from os import system
from utilidadescv import moeda
from utilidadescv import dado
system("cls")
print()

n = dado.leiaDinheiro("Digita o preço: kzs:")
moeda.resumo(n, 35, 22)