from os import system
from datetime import datetime 
system("cls")
print()

ano_atual = datetime.now().year

dados = {}

dados["Nome"] = input("Nome: ")
data = int(input("Data de nascimento: "))
dados["Idade"] = ano_atual - data
dados["Carteira de trabalho"] = int(input("Digita carteira de trablho [0 não tem]: "))
if dados["Carteira de trabalho"] == 0:
    pass
else:
    dados["Ano de contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário: kzs "))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Ano de contratação"]) + 35) - ano_atual
print("=-" * 40)
for k, v in dados.items():
        print(f" - {k} tem o valor {v}")