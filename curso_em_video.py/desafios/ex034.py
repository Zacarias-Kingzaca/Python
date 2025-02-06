from os import system
system ("cls")
print()

salario = float(input("\033[1mFuncionário qual é o seu salário kzs:\033[m "))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print("Quem ganhava \033[1;31m{:.2f}\033[m kzs passa a ganhar \033[1;32m{:.2f}kzs\033[m".format(salario,novo))