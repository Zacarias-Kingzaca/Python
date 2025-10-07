from os import system
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


