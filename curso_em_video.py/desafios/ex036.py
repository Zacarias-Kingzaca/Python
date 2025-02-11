from os import system
system ("cls")
print()


casa = float(input("Digita o valor da casa: Kzs "))
salario = float(input("Salário do comprador: Kzs "))
anos =int(input("Digita anos de financiamento? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print("Para pagar uma casa de Kzs{:.2f} em {} anos a prestação será de Kzs{:.2f}".format(casa, anos, prestacao))

if prestacao <= minimo:
    print("\033[32m Empréstimo Concedido!\033[m")
else:
    print("\033[31mEmpréstimo Negado! \033[m")