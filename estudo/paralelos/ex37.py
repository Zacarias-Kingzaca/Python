from os import system
from op import operacao
system("cls")
print()


class Item:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


class Estoque:
    def __init__(self):
        self.lista = []


    def adicionar_item(self, item):
        self.lista.append(item)


    def retirar_item(self, item):
        encontrou = False
        for i in self.lista:
            if i.nome.lower() == item.lower():
                encontrou = True
                self.lista.remove(i)
                print("Item removido com sucesso!")
        if not encontrou:
            print("Item não encontrado.")


    def ver_estoque(self):
        try:
            for i in self.lista:
                print(f"Produto: {i.nome}")
                print(f"Quantidade: {i.quantidade}")
                print("===============================")          
        except:
            print("Nenhum produto encontrado!")


produto = Estoque()

while True:
    print("1 - Adicionar Item")
    print("2 - Retirar Item")
    print("3 - Ver estoque")
    print("4 - Sair")
    op = input("Escolha: ")

    if op == "1":
        system("cls")
        nome = input("Nome do produto: ").strip().title()
        quantidade = int(input("Quantidade: ").strip())
        p = Item(nome, quantidade)
        produto.adicionar_item(p)
        operacao()

    elif op == "2":
        system("cls")
        nome = input("Nome do produto a ser deletado: ")
        produto.retirar_item(nome)
        operacao()

    elif op == "3":
        system("cls")
        produto.ver_estoque()
        operacao()

    elif op == "4":
        system("cls")
        break
    
    else:
        print("Escolha errada!")
        