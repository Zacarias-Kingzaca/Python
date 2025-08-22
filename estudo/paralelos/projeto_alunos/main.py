from os import system
from sistema.cadastro import cadastrar_aluno
from sistema.relatorio import relatorio
from time import sleep
system("cls")
print()
while True:

    print("\033[1;36m*\033[m"*40)
    print(f"{"\033[1mCADASTRAR ALUNO\033[m":^47}")
    print("\033[1;36m*\033[m"*40)

    print("""\033[1;36m
    [ 1 ] - Cadastrar aluno
    [ 2 ] - Gerar relatório
    [ 3 ] - Sair
    \033[m""")

    op = input("-> ")
    
    if op not in ["1", "2", "3"]:
       system("cls")
       print("\033[1;31mOpção inválida, espere 5 segundos para retornar ao menu.\033[m")
       sleep(5)
       system("cls") 
    elif op == "1":
        system("cls")
        sleep(1)
        print("\033[1;36m*\033[m"*40)
        print(f"{"\033[1mCADASTRAR ALUNO\033[m":^47}")
        print("\033[1;36m*\033[m"*40)
        cadastrar_aluno()
        sleep(3)
        system("cls")
    elif op == "2":
        system("cls")
        sleep(1)
        relatorio()
        while True:
            sleep(1)
            voltar = input("Deseja voltar ao menu? [Sim (s) /Não (n)]: ").strip().upper()
            if voltar in "SIMS":
                system("cls")
                break
            elif voltar in "NÃON":
                 system("cls")
                 sleep(1)
                 exit()
            else:
                print("\033[1;31mValor inválido digite apenas [Sim (s) /Não (n)]\033[m")
                sleep(4)
    elif op == "3":
        system("cls")
        sleep(1)
        break
    