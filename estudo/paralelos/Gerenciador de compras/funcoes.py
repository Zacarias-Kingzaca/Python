from os import system

carrinho = []

def add():
    print("="*30)
    print(f"{"Adicionar Produto":^30}")
    print("="*30)
    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço - kzs: "))
    except:
        print("\033[1;31mErro ao tentar adicionar produto...\033[m")
    else:
        print("\033[1;32mProduto adicionado com sucesso!\033[m")
        carrinho.append({"Nome": nome, "Preço": preco})


def listar():
    print("="*30)
    print(f"{"Lista de Produtos":^30}")
    print("="*30)
    print(f"{"Nome":<15} {"Preço":>10}")
    print()
    encontrou = False
    for i in carrinho:
        print(f"Nome: {i["Nome"]:<15}".title(), end="")
        print(f"Preço: - kzs {i["Preço"]:<10.2f}")
        encontrou = True
    if not encontrou:
        print("\033[1;31mNenhum produto cadastrado...\033[m")


def remover_por_nome():
    print("="*30)
    print(f"{"Remover produto por nome":^30}")
    print("="*30)
    nome = input("Digita o nome do produto: ")
    for i in carrinho:
        if i["Nome"].lower() == nome.lower():
            carrinho.remove(i)
            print("\033[1;32mProduto removido com sucesso!\033[m")
            break
    else:
        print("\033[1;31mProduto não encontrado!\033[m")


def produto_mais_caro_barato():
    print("="*50)
    print(f"{"Produto mais caro e o mais barato":^50}")
    print("="*50)
    try:
        caro = max(carrinho, key=lambda x: x['Preço'])
        barato = min(carrinho, key=lambda x: x['Preço'])
        print(f"O produto mais caro é {caro["Nome"]}  custa - kzs {caro["Preço"]:.2f}")
        print(f"O produto mais barato é {barato["Nome"]}  custa - kzs {barato["Preço"]:.2f}")
    except:
        print("\033[1;31mNenhum produto cadastrado...\033[m")


def ordenar():
    print("="*30)
    print(f"{"Lista ordenada":^30}")
    print("="*30)
    print("1 - Ordenar por nome")
    print("2 - Ordenar por preço")
    op = input("Escolha: ")
    print(f"{"Nome":<15} {"Preço":>10}")
    encontrou = False
    if op == "1":
        ordem = sorted(carrinho, key=lambda x: x["Nome"])
        for o in ordem:
            print(f"Nome: {o["Nome"]:<15}".title(), end="")
            print(f"Preço: - kzs {o["Preço"]:<10.2f}")
            encontrou = True
        if not encontrou:
            system("cls")
            print("\033[1;31mNenhum produto cadastrado...\033[m")


    if op == "2":
        ordem = sorted(carrinho, key=lambda x: x["Preço"])
        for o in ordem:
            print(f"Nome: {o["Nome"]:<15}".title(), end="")
            print(f"Preço: - kzs {o["Preço"]:<10.2f}")
            encontrou = True
    if not encontrou:
        system("cls")
        print("\033[1;31mNenhum produto cadastrado...\033[m")
        

def limpar():
    carrinho.clear()
    print("\033[1;32mLista apagada com sucesso!\033[m")