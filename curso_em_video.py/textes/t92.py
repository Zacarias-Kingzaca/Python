from os import system
system("cls")
print()
s = float(input("Sálario mensal: "))
g = float(input("Gastos mensal fixo: "))
salario = s * 12
gastos = g * 12
economia = salario - gastos
print(f"Económia anula:{economia:.2f}kzs")