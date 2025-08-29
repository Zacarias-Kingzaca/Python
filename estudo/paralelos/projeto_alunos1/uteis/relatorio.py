from centralizar import center

def geral():
    center("\033[1;35m      =========================================\033[m")
    center("\033[1;35m       RELATÓRIO GERAL\033[m")
    center("\033[1;35m      =========================================\033[m")
    print()

    try:
        with open("aluno1.txt", "r", encoding="UTF-8") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except:
        print("\033[mArquivo não encontrado.\033[m")
    
        