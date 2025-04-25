from os import system
from datetime import date
system("cls")
print()

ano = date.today().year
usuario = int(input("Digita o ano em que nasceste: "))

permissao = ano - usuario

if permissao >= 18:
    print("CIDADÃO APROVADO PARA VOTAR")
else:
    print("CIDADÃO REPROVADO PARA VOTAR.")