from os import system
import requests
system("cls")
print()


#EX1
headers = {
    "User-Agent": "meu-aprendizadi-python"
}

res = requests.get("https://api.github.com/users/Zacarias-kingzaca", headers=headers)
print(res.json())
print()
print()

#EX2
headers = {
    "Accept-Language": "fr"
}

res = requests.get("https://httpbin.org/headers", headers=headers)
print(res.json())
print()
print()

#EX3
headers = {
    "User-Agent": "aprendendo-requests",
    "Accep": "application/vnd.github+json"
}

res = requests.get("https://api.github.com/repos/python/cpython", headers=headers)
print(f"Name: {res.json()["name"]}")
print(f"Stargazers_count: {res.json()["stargazers_count"]}")
