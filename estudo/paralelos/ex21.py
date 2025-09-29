from os import system
from functools import reduce
system("cls")
print()

produtos = [
            {"nome": "Mouse",  "preço":  2000},
            {"nome": "Teclado", "preço": 1000},
            {"nome": "Monitor", "preço": 3000}
            ] 
print("=======================================")
print("           Preços Normais")
print("=======================================")
print()
for i, p in enumerate(produtos):

    for i,j in p.items():
        print(f"{i}:{j}", end="\n")
    print("===============================")
print()
desconto = int(input("Digita percentagem de desconto desconto : %"))
nova = list(map(lambda x: {"nome": x["nome"], "preço com desconto": x["preço"] - x["preço"] * desconto / 100}, produtos))
print()
print("=======================================")
print("         Preços com descontos")
print("=======================================")
print()
for i in nova:
    for i,j in i.items():
        print(f"{i}: {j}")
    print("===============================")