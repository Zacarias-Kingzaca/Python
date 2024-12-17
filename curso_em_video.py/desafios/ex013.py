from os import system
system ("cls")
print()

salario = float(input("Qual é o salário do Funcionário? kzs"))

novo = salario + (salario * 15 / 100)

print("Um funcionário que ganhava kzs{:.2f}, com o aumento, passa a receber kzs{:.2f}".format(salario,novo))