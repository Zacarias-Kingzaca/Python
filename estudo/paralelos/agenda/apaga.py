def apagar_contato():
    print()
    print("==================APAGAR CONTATO==================")
    try:
        while True:
            try: 
                nome = input("Nome: ").title().strip()
            except:
                print("Aconteceu um erro, tente novamente")
            else:
                break
        with open("contatos.txt", "r", encoding="utf") as arquivo:
            linhas = arquivo.readlines()
            novo_bloco = []
            encontrou = False
            nao = False
            for linha in linhas:
                 if linha.startswith("Nome:"):
                      if f"Nome: {nome}" in linha.strip():
                           print("\033[1;32mContato removido com sucesso!\033[m")
                           nao = True
                           encontrou = True
                           continue
                      else:
                           encontrou = False
                 if not encontrou:
                    novo_bloco.append(linha)
        if not nao:
                print("\033[1;31mContato não encontrado.\033[m")
        with open("contatos.txt", "w", encoding="utf") as arquivo:
                arquivo.writelines(novo_bloco)
    except:
        print("\033[1;31mErro ao acessar a base de dados.\033[m")