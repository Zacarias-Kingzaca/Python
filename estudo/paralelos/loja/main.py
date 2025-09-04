from os import system
from cadastrar import cadastrar_produto
from listar import listra_produto
from op import operacao
system("cls")
print()


while True:
    print("========================================")
    print("                 MENU")
    print("========================================")
    print(" - 1 Cadastrar Produto")
    print(" - 2 Ver Produtos")
    print(" - 3 Adicionar ao carrinho")
    print(" - 4 Ver carrinho")
    print(" - 5 Finalizar compra")
    print()
    op = input("-: ")

    if op not in ["1", "2", "3", "4", "5"]:
        print("\033[1;31mOpção inválida.\033[m")
        op = input("-: ")
    
    elif op ==  "1":
        system("cls")
        cadastrar_produto()
        operacao()

    elif op == "2":
        system("cls")
        listra_produto()
        operacao()
    
    elif op == "3":
        system("cls")
        operacao()
    