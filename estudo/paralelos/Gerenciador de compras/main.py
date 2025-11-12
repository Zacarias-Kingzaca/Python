from os import system
from op import operacao
from funcoes import add
from funcoes import listar
from funcoes import remover_por_nome
from funcoes import produto_mais_caro_barato
from funcoes import ordenar
from funcoes import limpar
system("cls")
print()


while True:
    system("cls")
    print("*"*50)
    print(f"{"LOJA ZACARIAS":^50}")
    print("*"*50)
    print("1. Adicionar Produto")
    print("2. Ver lista de produtos")
    print("3. Romover por nome")
    print("4. Produto mais caro/barato")
    print("5. Ordenar por nome/preço")
    print("6. Limpar lista")
    print("0. Sair")
    op = input("Escolha: ")

    if op == "1":
        system("cls")
        add()
        operacao()
    elif op == "2":
        system("cls")
        listar()
        operacao()
    elif op == "3":
        system("cls")
        remover_por_nome()
        operacao()

    elif op == "4":
        system("cls")
        produto_mais_caro_barato()
        operacao()

    elif op == "5":
        system("cls")
        ordenar()
        operacao()

    elif op == "6":
        system("cls")
        limpar()
        operacao()

    elif op == "0":
        system("cls")
        break



