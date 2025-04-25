from os import system
system("cls")
print()

consumo = float(input("Quantos Kwh foi consumido este mês? "))
preco = float(input("Qual é o preco a pagar por cada Kwh? "))
total = consumo * preco
print(f"O preço a pagar será de {total:.2f}kzs")