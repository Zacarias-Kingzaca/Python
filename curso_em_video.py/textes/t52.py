from os import system
system("cls")
print("")
print(30*"=")
print("{:^30}".format("CALCULO DE DESCONTO"))
print(30*"=")

preco = float(input("DIGITA O PREÇO DO PRODUTO: "))
desconto = float(input("DIGITA A PERCENTAGEM: "))
vdc = (desconto / 100) * preco
precof = preco - vdc
print(f"O produto vai consturar {precof:.2f}kzs")