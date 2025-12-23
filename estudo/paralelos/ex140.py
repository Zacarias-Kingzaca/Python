from os import system
import requests
system("cls")
print()

print("EX 1 - MOSTRAR 5 NOMES COMPLETOS DE USUÁRIOS ALIATÓRIOS")
try:
    res = requests.get("https://randomuser.me/api/?results=5")
    dados = res.json()

    for usuario in dados["results"]:
        nome = usuario["name"]
        print(nome["title"], nome["first"], nome["last"])
    print()
except:
    print("Erro ao tentar acessar a API.")

print("EX 2 - MOSTRAR 10 NOMES COMPLETOS DE USUÁRIOS ALIATÓRIOS DO GÊNERO FEMENINO")
try:
    params = {
        "results": 10,
        "gender": "female"
    }
    res = requests.get("https://randomuser.me/api/", params=params)
    dados = res.json()

    for usuario in dados["results"]:
        nome = usuario["name"]
        genero = usuario["gender"]
        print(f"Nome:", nome["title"], nome["first"], nome["last"],  "|", f"Gênero: {genero}")
    print()
except:
    print("Erro ao tentar acessar a API.")

print("EX 3 - MOSTRAR 10 NOMES COMPLETOS DE USUÁRIOS ALIATÓRIOS DO GÊNERO MASCULINO COM SEUS E-MAILS E PAÍS")
try:
    params = {
        "results": 10,
        "gender": "male"
    }
    res = requests.get("https://randomuser.me/api/", params=params)
    dados = res.json()

    for usuario in dados["results"]:
        nome = usuario["name"]
        genero = usuario["gender"]
        email = usuario["email"]
        nat = usuario["location"]["country"]
        print(f"Nome:", nome["title"], nome["first"], nome["last"],  "|", f"Gênero: {genero}" "|", f"E-mail: {email}" "|", f"País: {nat}")
    print()
except:
    print("Erro ao tentar acessar a API.")

print("EX 4 - CRIAR UMA LISTA COM NOMES COMPLETOS DE USUÁRIOS ALIATÓRIOS")
try:
    res = requests.get("https://randomuser.me/api/?results=5")
    dados = res.json()
    nomes = []
    for usuario in dados["results"]:
        nome = usuario["name"]
        n = nome["title"], nome["first"], nome["last"]
        nomes.append(n)
    print("="*40)
    print(f"{"LISTA DE NOMES":^40}")
    print("="*40)
    for n in nomes:
        print(n)
    print()
except:
    print("Erro ao tentar acessar a API.")
