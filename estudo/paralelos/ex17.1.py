from os import system
system("cls")
print("")


def operacao():
    while True:
            per = input("Voltar para o menu? [Sim(s)/Não(n)]: ").strip().upper()
            if per in ["SIM","S"]:
                system("cls")
                break
            elif per in ["NÃO", "N"]:
                system("cls")
                exit()
            else:
                system("cls")
                print("\033[1;31mErro digite apenas [Sim(s)/Não(n)].\033[m")


def listra_produto():
    print("========================================")
    print("           LISTA DE PRODUTOS")
    print("========================================")

    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        print(conteudo)
    except:
        print("\033[1;31mErro ao tentar conectar-se com a Base de dados.\033[m\n")

def cadastrar_produto():
    print("========================================")
    print("           CADASTRAR PRODUTO")
    print("========================================")
    try:
        nome = input("Nome: ").capitalize().title()
        preco = float(input("Preço: ").strip())

        while True:
            cod = int(input("Código: ").strip())
            encontrou = False
            with open("produtos.txt", "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.readlines()
            bloco = []
            for linha in conteudo:
                bloco.append(linha)
                if "*******************************************" in linha.strip():
                  for dado in bloco:
                     if dado.startswith("Código:") and f"Código: {cod}" in dado:
                         print(f"\033[1;31mO código {cod} ja pertence a um produto.\033[m")
                         encontrou = True
                         break
                  bloco = []
                  if encontrou:
                      break
            if not encontrou:
                break
    except:
        print("\033[1;31mErro ao tentar conectar-se com a Base de dados.\033[m\n")
    else:
        with open("produtos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Código: {cod}\nNome: {nome}\nPreço: {preco:.2f}\n")
            arquivo.write("*******************************************\n")
            print("\033[1;32mProduto cadastrado com sucesso!\033[m")


carrinho = []

def adicionar_carrinho():
    print("========================================")
    print("         ADICIONAR AO CARRINHO")
    print("========================================")
    try:
       cod = input("Digita o código do produto: ").strip()

       with open("produtos.txt", "r", encoding="utf-8") as arquivo:
           linhas = arquivo.readlines()

       bloco = []
       for linha in linhas:
           bloco.append(linha)
           if "*******************************************" in linha.strip():
               for dado in bloco:
                   if dado.startswith("Código:"): 
                        codigo_produto = dado.replace("Código:", "").strip()
                        if codigo_produto == cod:
                            carrinho.append(bloco[:])
                            print("\033[1;32mProduto adicionado ao carrinho!\033[m")
                            return 
               bloco = []

       print("\033[1;31mProduto não encontrado.\033[m")    

    except:
        print("\033[1;31mErro ao tentar conectar-se com a Base de dados.\033[m\n")


def ver_carrinho():
    print("========================================")
    print("              CARRINHO")
    print("========================================")

    try:
        tot = 0
        if carrinho == []:
           print("O carrinho está vazio.")
        else:
          for linha in carrinho:
            for produto in linha:
                print(produto, end="")
        
          for linha in carrinho:
            for produto in linha:
             if produto.startswith("Preço:"):
                dado = float(produto.replace("Preço:", "").strip())
                tot += dado
        print(f"Total da compra: {tot:.2f}")
    except:
        print("\033[1;31mErro ao tentar conectar-se com a Base de dados.\033[m\n")        


def finalizar():
    print("========================================")
    print("          FINALIZAR COMPRA")
    print("========================================")
    tot = 0
    if carrinho == []:
        print("O carrinho está vazio.")
    else:
        for linha in carrinho:
            for produto in linha:
                if produto.startswith("Preço:"):
                    dado = float(produto.replace("Preço:", "").strip())
                    tot += dado
        print("Compra finalizada!")
        print(f"Total: {tot:.2f}")
        print("Obrigado pela sua compra!")
        carrinho.clear()
        
                          
while True:
    print("========================================")
    print("                 MENU")
    print("========================================")
    print(" - 1 Cadastrar Produto")
    print(" - 2 Ver Produtos")
    print(" - 3 Adicionar ao carrinho")
    print(" - 4 Ver carrinho")
    print(" - 5 Finalizar compra")
    print(" - 6 Sair")
    print()
    op = input("-: ")

    if op not in ["1", "2", "3", "4", "5", "6"]:
        print("\033[1;31mOpção inválida.\033[m")
        op = input("-: ")
    
    elif op ==  "1":
        system("cls")
        cadastrar_produto()
        operacao()

    elif op == "2":
        system("cls")
        listra_produto()
        operacao()
    
    elif op == "3":
        system("cls")
        adicionar_carrinho()
        operacao()

    elif op == "4":
        system("cls")
        ver_carrinho()
        operacao()

    elif op == "5":
        system("cls")
        finalizar()
        operacao()
    
    elif op == "6":
        system("cls")
        break