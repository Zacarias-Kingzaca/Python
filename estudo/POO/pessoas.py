from os import system 
system("cls")
print("")

from estudo.POO.paii import Papa
from estudo.POO.filhoo import Filho

filho = Filho()
filho.estudar()


print(60* "=")
print("o Nome do filho é ",filho.nome)
print("Ele tem ",filho.idade,"anos")
print("Pesa",filho.peso,"Kg")
print(filho.n_ir_a_escola)
print(filho.Mesada())
print(filho.trabalhar())
print(filho._Pai__Segredo())
print(60* "=")
