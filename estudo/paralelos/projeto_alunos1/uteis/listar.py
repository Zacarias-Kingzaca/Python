from os import system
from centralizar import center
from time import sleep
system("cls")
print()

def lista():
    center("\033[1;35m      =========================================\033[m")
    center("\033[1;35m       LISTAR ALUNOS\033[m")
    center("\033[1;35m      =========================================\033[m")
    print()

    print("""\033[1;35m
    [ 1 ] - Alunos aprovados
    [ 2 ] - Alunos reprovados
    [ 3 ] - Todos
    \033[m""")
    
    while True:
         op = input("-:> ").strip()
         if op not in ["1", "2", "3"]:
            sleep(0.8)
            system("cls")
            print("\033[1;31mOpção inválida, espere 5 segundos para voltar para o menu.\033[m")
            sleep(7)
            system("cls")
            
         if op == "1":
            system("cls")
            center("\033[1;35m      =========================================\033[m")
            center("\033[1;35m       ALUNOS APROVADOS\033[m")
            center("\033[1;35m      =========================================\033[m")
            print()
            try:
                with open("aluno1.txt", "r", encoding="UTF-8") as arquivo:
                    linhas = arquivo.readlines()
                    bloco = []
                    encontrou = False
                    for linha in linhas:
                        if linha.strip() == "":
                            continue
                        bloco.append(linha)
                        if "==========================================".strip() in linha:
                            for dado in bloco:
                                    if "Situação: Aprovado" in dado:
                                        for item in bloco:
                                            if item.startswith("Nome:"):
                                                print(f"{item.strip()} - Aprovado")
                                                encontrou = True
                            bloco = []                                                            
                    if not encontrou:
                        print("\033[1;31mNenhum aluno encontrado\033[m")  
                break         
            except:
                    print("\033[1;31mConexão não establecida com a Base de dados\033[m")

         if op == "2":
            system("cls")
            center("\033[1;35m      =========================================\033[m")
            center("\033[1;35m       ALUNOS REPROVADOS\033[m")
            center("\033[1;35m      =========================================\033[m")
            print()

            try:
                with open("aluno1.txt", "r", encoding="UTF-8") as arquivo:
                    linhas = arquivo.readlines()
                    bloco = []
                    encontrou = False
                    for linha in linhas:
                        if linha.strip() == "":
                            continue
                        bloco.append(linha)
                        if "==========================================".strip() in linha:
                            for dado in bloco:
                                if "Situação: Reprovado" in dado:
                                    for item in bloco:
                                        if item.startswith("Nome:"):
                                            print(f"{item.strip()} - Reprovado")
                                            encontrou = True
                                    break
                            bloco = []
                    if not encontrou:
                        print("\033[1;31mNenhum aluno encontrado\033[m") 
                break
            except:
                print("\033[1;31mConexão não establecida com a Base de dados\033[m")
         if op == "3":
            system("cls")
            center("\033[1;35m      =========================================\033[m")
            center("\033[1;35m       LISTAR ALUNOS\033[m")
            center("\033[1;35m      =========================================\033[m")
            print()

            try:
                with open("aluno1.txt", "r", encoding="UTF-8") as arquivo:
                    linhas = arquivo.readlines()
                    encontrou = False
                    bloco = []
                    for linha in linhas:
                        if linha.strip() == "":
                            continue
                        bloco.append(linha)
                        if "==========================================".strip() in linha:
                                for dado in bloco:
                                    if "Situação: Aprovado" in dado:
                                        for item in bloco:
                                            if item.startswith("Nome:"):
                                                print(f"{item.strip()} - Aprovado")
                                                encontrou = True
                                    if"Situação: Reprovado" in dado:
                                        for item in bloco:
                                            if item.startswith("Nome:"):
                                                print(f"{item.strip()} - Reprovado")
                                                encontrou = True
                                        break
                                bloco = []
                    if not encontrou:
                            print("\033[1;31mNenhum aluno encontrado\033[m") 
                break               
            except:  
                print("\033[1;31mConexão não establecida com a Base de dados\033[m")                