from os import system
from moeda import dobro
from moeda import aumentar
from moeda import diminuir
from moeda import metade
from moeda import moeda
system("cls")
print()


n = int(input("Digita o preço kzs: "))
print(f"A metade de {moeda(n)} é: {moeda(metade(n))}")
print(f"O dobro de {moeda(n)} é o: {moeda(dobro(n))}")
print(f"O aumento de 10% temos: kzs{moeda(aumentar(n, 10))}")
