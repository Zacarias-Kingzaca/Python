from os import system
import requests
system("cls")
print()

data = {"title": "Novo post", "body": "Conteúdo", "userId": 1}
res = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(res.json())