from os import system
import requests
system("cls")
print()

#EX1
dados = {
    "Produto": "Livro",
    "Preço": 2000.00
}

headers = {
    "x-loja-id": "001",
    "Content-Type": "application/json"
}

res = requests.post("https://httpbin.org/post", json=dados, headers=headers)
print(res.json())
print()

