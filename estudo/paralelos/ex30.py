from os import system
from op import operacao
system("cls")
print()

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    
class Vendas():
    def __init__(self):
        self.Produto = []

    def adicionar_produto(self, produto):
        self.Produto.append(produto)

    def total_venda(self):
        total = 0
        for p in self.Produto:
            total += p.preco * p.quantidade
            system("cls")
            print(f"O total dos produtos é {total:.2f}kzs")


loja = Vendas()

while True:

    print("1- Adicionar Produto")
    print("2- Total de venadas ")
    print("4- Sair ")
    op = input("-: ")

    if op == "1":
        system("cls")
        nome = input("Nome do produto: ").title()
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))
        p = Produto(nome, preco, quantidade)
        loja.adicionar_produto(p)
        operacao()

    elif op == "2":
        system("cls")
        total = loja.total_venda()
        operacao()

    elif op == "3":
        system("cls")
        break

    else:
        print("Opção errada!")