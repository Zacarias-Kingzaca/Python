from os import system
system("cls")
print()

class Produto:
    def __init__(self, nome, preco):
        self.nome  = nome
        self.preco = preco

    def Info(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco:.2f} kzs")


class Produto_alimenticio(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def Info(self):
        super().Info()
        print("Valído até: 12/02/2027")


class Produto_eletronico(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def Info(self):
        super().Info()
        print("Garantia de: 1 ano")


p1 = Produto_alimenticio("arroz", 20000)
p1.Info()
p2 = Produto_eletronico("carro", 10000000)
p2.Info()