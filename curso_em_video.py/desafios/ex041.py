from os import system
system ("cls")
print()
from datetime import date

atual = date.today().year
ano = int(input("Digita o teu ano de nascimento: "))

idade = atual - ano
print ("O atleta tem {} anos.".format(idade))

if idade <= 9:
    print("Classificação: MIRIM")

elif idade <= 14:
    print("Classificação: INFANTIL")

elif idade <= 19:
    print("Classificação: JUNIOR")
    
elif idade <= 25:
    print("Classificação: SÊNIOR")

else:
    print("Classificação: MASTER")