from os import system
system("cls")
print()

valorp = int(input("Digita o valor principal: "))
taxa = int(input("Digita a taxa de juros mensal: "))
meses = int(input("Digita o número de meses: "))
taxa1 = taxa / 100 
totvalor = valorp * (1 + taxa1 + meses)
print(f"O valor total a ser pago será de {totvalor:.2f}kzs")