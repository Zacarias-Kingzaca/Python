from os import system
import requests
system("cls")
print()

url = "https://randomuser.me/api/"
for pagina in range(1, 3):
    res = requests.get(url,params={"results": 3, "page": pagina})
    dados = res.json()["results"]
    for i in dados:
        nome = f"{i["name"]["first"]}  {i["name"]["last"]}"
        email = f"{i["email"]}"
        print(f"Página {pagina} | Nome: {nome} | E-mail: {email}")
        print()
