from os import system
import requests
system("cls")
print()

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Authorization": "Bearer SEU_TOKEN_AQUI"
}
res = requests.get("https://httpbin.org/headers",headers=headers)
print(res.status_code)
print(res.json())
