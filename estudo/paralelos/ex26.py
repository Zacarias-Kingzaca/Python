from os import system
system("cls")
print()

class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_p(self, produto):

        for p in self.produtos:
            if p.nome.lower() == produto.nome.lower():
                p.quantidade += produto.quantidade
                return
        else:
            self.produtos.append(produto)

    def listar_p(self):
        for p in self.produtos:
            print(f"Produto: {p.nome}\nPreço: {p.preco}kzs \nQuantidade: {p.quantidade}")
            print("===============================")

    def buscar_p(self,nome):
    
        for p in self.produtos:
            if p.nome.lower() == nome.lower():
               print(f"Produto: {p.nome}\nPreço: {p.preco}kzs \nQuantidade: {p.quantidade}")
               return
        print("Produto não encontrado")



estoque = Estoque()
p1 = Produto("arroz", 500, 5)
p2 = Produto("feijão", 600, 3)
p3 = Produto("arroz", 500, 2)
estoque.adicionar_p(p1)
estoque.adicionar_p(p2)
estoque.adicionar_p(p3) 
estoque.listar_p()
estoque.buscar_p("arrozz")