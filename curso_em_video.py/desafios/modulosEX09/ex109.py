from os import system
from moeda import dobro
from moeda import aumentar
from moeda import diminuir
from moeda import metade
from moeda import moeda
system("cls")
print()


n = int(input("Digita o preço kzs: "))
print(f"A metade de {moeda(n)} é: {(metade(n, True))}")
print(f"O dobro de {moeda(n)} é o: {(dobro(n, True))}")
print(f"O aumento de 10% temos: {(aumentar(n, 10, True))}")
print(f"A redução de  13% temos: {diminuir(n, 13, True)}")
