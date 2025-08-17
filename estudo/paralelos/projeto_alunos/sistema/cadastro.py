from os import system
def cadastrar_aluno():
    fechar =  False
    nome = input("Nome: ").title()
    while True:
        try:
            Nota1 = float(input("Primeira nota: "))
            Nota2 = float(input("Segunda nota:  "))
            print("\033[1;32mCadastrado com sucesso!\033[m")
        except ValueError:
            system("cls")
            print("\033[1;31mValor inválido. Use apenas números.\033[m")
        else:
            media = (Nota1 + Nota2 ) / 2
            if media >= 10:
                situcao = 'Aprovado'
                fechar = True
                with open('aluno.txt', 'a', encoding="UTF-8") as arquivo:
                    arquivo.write(f'Nome: {nome}\nNota1: {Nota1}\nNota2: {Nota2}\nSituação: {situcao}\n')
                    arquivo.write("==========================================\n")
            else:
                situcao = 'Reprovado'
                fechar = True
                with open('aluno.txt', 'a', encoding="UTF-8") as arquivo:
                    arquivo.write(f'Nome: {nome}\nNota1: {Nota1}\nNota2: {Nota2}\nSituação: {situcao}\n')
                    arquivo.write("==========================================\n")
        if fechar == True:
            break
