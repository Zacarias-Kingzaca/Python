from os import system
system ("cls")
print()

salario = float(input("Funcionário qual é o seu salário kzs: "))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print("Quem ganhava {:.2f}kzs passa a ganhar {:.2f}kzs".format(salario,novo))