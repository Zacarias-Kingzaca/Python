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