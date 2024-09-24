from os import system 
system("cls")
print("")

from canecas.caneca import Caneca
from canecas.canecazaca import CanecaZaca
from canecas.canecaking import CanecaKing

Canecazaca = CanecaZaca()
Canecazacarias = Caneca("Caneca zacarias", "Brasil", "Amarela")
canecaking = CanecaKing()

print("Preços")
print()
print(f"A {Canecazaca.nome} tem o preço de {Canecazaca.preco} KZ")
print(f"A {Canecazacarias.nome} tem o preço de {Canecazacarias.preco} KZ")
print(f"A {canecaking.nome} tem o preço de {canecaking.preco} KZ")

print(Canecazacarias._Caneca__preco_fabrico)