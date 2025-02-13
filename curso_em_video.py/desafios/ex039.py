from os import system
system ("cls")
print()
from datetime import date

atual = date.today().year
nasc = int(input("Em que ano voçe nasceu? "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))

if idade == 18:
    print("Voçê tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo =  18 - idade
    print("Ainda falta {} anos para o alistamento.".format(saldo))
    ano = atual + saldo
    print("Seu alistamento ser em {} anos".format(ano))
elif idade > 18:
    saldo = idade -18
    print("Voçê já deveria se alistar há {}".format(saldo))
    ano = atual - saldo
    print("Sue alistamento foi em {}".format(ano))