from os import system
from uteis.cadastrar import cadastrar_aluno
from uteis.boletim import consultar_boletim
from time import sleep
from centralizar import center
system("cls")
print()

while True:
    center("\033[1;35m      =========================================\033[m")
    center("\033[1;35m       ESCOLA ZACARIAS\033[m")
    center("\033[1;35m      =========================================\033[m")
    print()
    print("""\033[1;35m
        [ 1 ] - Cadastrar aluno
        [ 2 ] - Consultar boletim
        [ 3 ] - Corrigir dados(nota/nome)
        [ 4 ] - Remover aluno
        [ 5 ] - Listar alunos aprovados/reprovados
        [ 6 ] - Relatório geral
        [ 7 ] - Sair do programa
    \033[m """)

    op = input("-:> ").strip()
    if op not in ["1", "2", "3", "4", "5", "6", "7"]:
        sleep(0.8)
        system("cls")
        print("\033[1;31mOpção inválida, espere 5 segundos para voltar para o menu.\033[m")
        sleep(7)
        system("cls")

    if op == "1":
        sleep(1)
        system("cls")
        cadastrar_aluno()
        while True:
            per = input("Voltar para o menu? [Sim(s)/Não(n)]: ").strip().upper()
            if per in ["SIM","S"]:
                system("cls")
                break
            elif per in ["NÃO", "N"]:
                system("cls")
                exit()
            else:
                system("cls")
                print("\033[1;31mErro digite apenas [Sim(s)/Não(n)].\033[m")

    if op ==  "2":
        sleep(1)
        system("cls")
        consultar_boletim()
        while True:
            per = input("Voltar para o menu? [Sim(s)/Não(n)]: ").strip().upper()
            if per in ["SIM","S"]:
                system("cls")
                break
            elif per in ["NÃO", "N"]:
                system("cls")
                exit()
            else:
                system("cls")
                print("\033[1;31mErro digite apenas [Sim(s)/Não(n)].\033[m")
    if op ==  "7":
        break
