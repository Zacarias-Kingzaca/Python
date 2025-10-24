from os import system
system("cls")
print("")

class Estoque:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

    
    def set_adicionar(self, quantidade):
        if quantidade > 0:
            self.__quantidade += quantidade
            print(f"{quantidade} Produtos adicionados.")
        else:
            print("Quantidade inválida")

    def set_remover(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida")
        elif self.__quantidade < quantidade:
            print(f"O estoque só se encontra com {self.__quantidade} produtos")
        else:
            self.__quantidade -= quantidade
            print(f"{quantidade} Produtos removidos.")

    def get_ver(self):
        print(f"Produto: {self.__produto}")
        print(f"Quantidade: {self.__quantidade}")


produto = Estoque("Carro", 6)
produto.set_adicionar(6)
produto.set_remover(10)
produto.get_ver()