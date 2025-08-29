from os import system
from time import sleep
from centralizar import center

def remover_aluno():
    system("cls")
    print()
    center("\033[1;35m      =========================================\033[m")
    center("\033[1;35m       REMOVER ALUNO\033[m")
    center("\033[1;35m      =========================================\033[m")
    print()

    while True:
                   
            try:
                 num = int(input("Nº de estudante: ").strip())
            except:
                    system("cls")
                    print("\033[1;31mIntroduz apenas números inteiros\033[m")
            else:
                 break
             
    try:
        with open("aluno1.txt", "r", encoding="UTF-8") as f:
            linhas = f.readlines()
        novo_conteudo = []
        remover_bloco = False
        for linha in linhas:
            if linha.startswith("Nº estudante:"):
                if linha.strip() == f"Nº estudante: {num}":
                    remover_bloco = True
                    sleep(1)
                    print(f"\033[1;32mo aluno {num} foi removido com sucesso.\033[m ")
                    continue #não adiciona linha
                else:
                    remover_bloco = False
            if not remover_bloco:
                novo_conteudo.append(linha)
        with open("aluno1.txt", "w", encoding="UTF-8") as f:
            f.writelines(novo_conteudo)
    except:
        print("\033[1;31mErro ao acessar a base de dados.\033[m")
