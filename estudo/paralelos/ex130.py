from os import system
import requests
system("cls")
print()

headers = {"User-Agent": "MeuAPP/1.0"}
res = requests.get("https://httpbin.org/headers", headers=headers)
print(res.json())