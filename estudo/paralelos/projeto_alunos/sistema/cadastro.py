from os import system
def cadastrar_aluno():
    class NomeError(Exception):
            pass
    fechar =  False
    while True:
        try:
                nome = input("Nome: ").title()
                nome.isalpha()
                if not nome.replace(" ","").isalpha():
                    system("cls")
                    raise NomeError("\033[1;31mO nome não pode conter números em algarismo ou símbolos.\033[m")
                break         
        except NomeError as r:
         print(r)
    while True:
        try:
            n1 = float(input("Primeira nota: "))
            n2 = float(input("Segunda nota:  "))
            print("\033[1;32mCadastrado com sucesso!\033[m")
        except ValueError:
            system("cls")
            print("\033[1;31mValor inválido. Use apenas números.\033[m")
        else:
            media = (n1 + n2 ) / 2
            if media >= 10:
                situcao = 'Aprovado'
                fechar = True
                with open('aluno.txt', 'a', encoding="UTF-8") as arquivo:
                    arquivo.write(f'Nome: {nome}\nNota1: {n1}\nNota2: {n2}\nSituação: {situcao}\n')
                    arquivo.write("==========================================\n")
            else:
                situcao = 'Reprovado'
                fechar = True
                with open('aluno.txt', 'a', encoding="UTF-8") as arquivo:
                    arquivo.write(f'Nome: {nome}\nNota1: {n1}\nNota2: {n2}\nSituação: {situcao}\n')
                    arquivo.write("==========================================\n")
        if fechar == True:
            break
