from os import system
system("cls")
print()

salario = float(input("Qula é o seu salário fixo? kzs"))
vendas = float(input("Qual é o valor de vendas que  realizaste no mês? kzs"))
comissao = vendas * 10/ 100
totsalario = salario + comissao
print(f"Funcionário o teu salário este mês será {totsalario:.2f}kzs")
