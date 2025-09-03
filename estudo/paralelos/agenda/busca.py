def buscar_por_nome():
    from os import system
    from time import sleep
    print()
    print("==================BUSCAR POR NOME==================")
    try:
        while True:
            try: 
                nome = input("Nome: ").title().strip()
            except:
                print("Aconteceu um erro, tente novamente")
            else:
                break
        encontrou = False
        with open("contatos.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            bloco = []
            for linha in linhas:
                if linha.strip() == "":
                    continue
                bloco.append(linha)
                if "==========================================" in linha:
                    for dado in bloco:
                        if f"Nome: {nome}" in dado:
                            print("\033[1;32mProcurando...\033[m")
                            sleep(3)
                            system("cls")
                            print("".join(bloco))
                            encontrou = True
                            break
                    bloco = []
                    if encontrou:
                        break
            if not encontrou:
             print("\033[1;31mContato não encontrado.\033[m")
    except:
        print("\033[1;31mErro ao acessar a base de dados.\033[m")