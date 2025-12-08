from os import system
system("cls")
import requests
print()

cep = "01001000"
resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
print(resposta.json())

if resposta.status_code == 200:
    dados = resposta.json()
    print(dados["logradouro"], "-", dados["bairro"])
else:
    print("Erro ao acessar a API")
