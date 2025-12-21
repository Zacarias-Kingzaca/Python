from os import system
import requests
system("cls")
print()

print("="*30)
print(f"{"Utilizando o método Post":^30}")
print("="*30)

print("Fazendo primeira requisição post.")
dados = {
    "nome": "Zacarias Eduardo João",
    "Idade": 22,
    "Altura": 1.82
}

res = requests.post("https://httpbin.org/post", json=dados)
print(res.json())
print()

print("Headers com requisição post.")

headers =  {
    "User-Agent": "Kingzaca/1.1",
    "Content-Type": "application/kingzaca"
}

res = requests.post("https://httpbin.org/post", json=dados, headers=headers)
print(res.json())
print()
