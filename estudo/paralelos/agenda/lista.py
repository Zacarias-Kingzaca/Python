def listar_contato():
    print("==================LISTA DE CONTATOS==================")
    try:
        with open("contatos.txt","r", encoding="utf") as arquivo:
            conteudo = arquivo.read()
        print(conteudo)
    except:
        print("\033[1;32mErro, ao tentar abrir a lista de contato.\033[m")