from os import system
import requests
system("cls")
print()

#EX1
token = "cm4m4jd79chgd9j3"

headers = {
    "Authorization": f"Bearer {token}"
}

res = requests.post("https://httpbin.org/post", headers=headers)
print(res.status_code)
print(res.text)
print()

#Requisição protegida

login_url = "https://httpbin.org/post"
dados_login = {
    "username": "admin",
    "password": "1234"
}

res_login = requests.post(login_url, json=dados_login)
token = res_login.json().get("token")

headers = {
    "Authorization": f"Bearer {token}"
}

res = requests.get("https://httpbin.org/headers", headers=headers)
print(res.text)

#Token expirado

token_valido = "SEU_TOKEN_AQUI"

headers = {
    "Authorization": f"Bearer {token_valido}"
}

res = requests.get("https://api.github.com/user", headers=headers)
data = res.json()
if res.status_code == 200 and data.get("authenticated") == True: 
    print(res.status_code)
    print("Token válido!")
else:
    print(res.status_code)
    print("Token inválido.")


#Headers adicionais

token = "123avcb475def"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "Application/json",
    "Accept-Language": "Pt-BR"
}

res = requests.get("https://httpbin.org/headers", headers=headers)
try:
    print(res.status_code)
    print(res.text)
except:
    print("Erro na API...")
