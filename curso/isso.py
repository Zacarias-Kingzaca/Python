from os import system
system("cls")
print("")

produtos = {}

for _ in range(3):
    id_produto = input("Digita o ID do produto: ")
    nome_produto = input("Digita o nome do produto: ")
    preco_produto = float(input("Digita o preço do produto: "))
    print()
    produtos[id_produto] = {'nome': nome_produto, 'preço kzs':preco_produto}
    print(f"Quantidade de produtos:{len(produtos)}")
    for id_ in produtos.items():
     print(f"ID:{id_}")
     print()

print("Todos os produtos foram adicionadso")