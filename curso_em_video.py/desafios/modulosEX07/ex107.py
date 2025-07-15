from os import system
from moeda import dobro
from moeda import aumentar
from moeda import diminuir
from moeda import metade
system("cls")
print()


n = int(input("Digita o preço kzs: "))
print(f"A metade de kzs{n} é: kzs{metade(n)}")
print(f"O dobro de kzs{n} é o: kzs{dobro(n)}")
print(f"O aumento de 10% temos: kzs{aumentar(n, 10)}")
