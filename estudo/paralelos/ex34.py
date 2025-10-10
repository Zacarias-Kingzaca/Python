from os import system
from time import sleep
system("cls")
print("")

produtos = ["Arroz", "Feijão","Macarrão", "Óleo"]
estoque = [10, 5, 6, 3]


nome_p = input("Nome do produto: ").strip().title()
quantidade_v = int(input("Quantidade vendida: ").strip())
encontrou = False
for i in produtos:
    if nome_p == i:
        pos = produtos.index(nome_p)
        estoque[pos] -= quantidade_v
        encontrou = True 
    
if not encontrou:
    system("cls")
    print("Nome não encontrado")

print(estoque)
 
