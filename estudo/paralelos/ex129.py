from os import system
import requests
system("cls")
print("")

params = {"results": 5}
res = requests.get("https://randomuser.me/api/", params=params)
for i, k in res.json().items():
    print(f"{i} = {k}")