from os import system
system("cls")
print("")
soma = 0
n =(input("Digita um valor:  "))
for digito in n:
    if digito.isdigit():
        soma += int(digito)
print(f"A soma dos digitos é {soma}")