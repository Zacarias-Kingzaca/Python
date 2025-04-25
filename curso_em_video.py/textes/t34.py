from os import system
system("cls")
print()

dias = int(input("Quantos dias ficou com o carro? "))
kmh = int(input("Qual foi a quilometragem percorrida? kmh "))
totdias = 60 * dias
totkmh = 0.15 * kmh
total = totdias + totkmh
print(f"A quantidade a ser paga é de {total:.2f}kzs")