from os import system
import requests
system("cls")
print()

res = requests.get("https://randomuser.me/api/?results=10")
dados = res.json()
usuarios = dados["results"]
for usuario in usuarios:
    nome = f"{usuario['name']['title']} {usuario['name']['first']} {usuario['name']['last']}"
    genero = usuario["gender"]
    email = usuario["email"]
    print("="*40)
    print(f"Nome: {nome}")
    print(f"Gênero: {genero}")
    print(f"E-mail: {email}")