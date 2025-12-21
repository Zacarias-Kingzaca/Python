from os import system
import requests
system("cls")
print()

print("User-Agente personalizado")
headers = {
    "User-Agent": "Kingzaca/1.0"
}
res = requests.get("https://httpbin.org/headers", headers=headers)
print(res.json())
print()

print("Authorization personalizado")

headers = {
    "Authorization": "Bearer MEU_TOKEN_EXEMPLO"
}
res = requests.get("https://httpbin.org/headers", headers=headers)
print(res.json())
print()

print("Enviar e ler headers personalizados")

headers = {
    "X-APP-Version": "2.5",
    "X-User-Language": "pt"
}
res = requests.get("https://httpbin.org/headers", headers=headers)
print(res.json())
print()