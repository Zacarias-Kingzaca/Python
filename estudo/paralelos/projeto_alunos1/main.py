from os import system
from uteis.cadastrar import cadastrar_aluno
from uteis.boletim import consultar_boletim
from uteis.remover import remover_aluno
from uteis.retificar import retificar_dado
from uteis.listar import lista
from uteis.relatorio import geral
from time import sleep
from centralizar import center
from op import operacao
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
        operacao()

    if op == "2":
        sleep(1)
        system("cls")
        consultar_boletim()
        operacao()
    
    if op == "3":
        sleep(1)
        system("cls")
        retificar_dado()
        operacao()
    
    if op == "4":
        sleep(1)
        system("cls")
        remover_aluno()
        operacao()

    if op == "5":
        sleep(1)
        system("cls")
        lista()
        operacao()

    if op == "6":
        sleep(1)
        system("cls")
        geral()
        operacao()

    if op == "7":
        sleep(1)
        system("cls")
        break
    