def relatorio():
    print("\033[1;36m*\033[m"*42)
    print(f"{"\033[1mRELATÓRIO DE ALUNOS\033[m":^49}")
    print("\033[1;36m*\033[m"*42)
    with open("aluno.txt", "r", encoding="UTF-8") as arquivo:
        print(arquivo.read())
        