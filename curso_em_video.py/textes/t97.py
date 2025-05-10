from os import system
system("cls")
print()
investimento = float(input("Digita o valor do investimento: "))
juros = float(input("Digita a taxa de juros anual: "))

vt = investimento * (1 + juros/100)
print(f"GANHO APÓS UM ANO :{vt:.2f}")