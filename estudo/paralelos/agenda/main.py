from os import system
from apaga import apagar_contato
from op import operacao
from nova import nova_tarefa
from lista import listar_contato
from busca import buscar_por_nome

system("cls")
print()
while True:
    print("==================AGENDA DE CONTATOS==================")

    print("1 - NOVO CONTATO")
    print("2 - LISTAR CONTATOS")
    print("3 - BUSCAR POR NOME")
    print("4 - APAGAR CONTATO")
    print("5 - SAIR")
    print()
    op = input("OPÇÃO: ").strip()
    
    if op not in ["1", "2", "3", "4", "5"]:
        print(f"\033[1;31m{op} não é uma opção válida.\033[m")
        op = input("OPÇÃO: ").strip()
    else:
     
     if op == "1":
        system("cls")
        nova_tarefa()
        operacao()

    if op == "2":
       system("cls")
       listar_contato()
       operacao()

    if op == "3":
       system("cls")
       buscar_por_nome()
       operacao()

    if op == "4":
       system("cls")
       apagar_contato()
       operacao()

    if op == "5":
       system("cls")
       break        
