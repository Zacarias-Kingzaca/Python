from os import system
from abc import ABC, abstractmethod
system("cls")
print()

class Produto(ABC):
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    @abstractmethod
    def calcular_preco(self):
        pass


class Eletronico(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def calcular_preco(self):
        imposto = self.get_preco() * 10 / 100
        return self.get_preco() + imposto
    
class Roupas(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def calcular_preco(self):
        imposto = self.get_preco() * 5 / 100
        return self.get_preco() + imposto
    

class Alimento(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def calcular_preco(self):
        imposto = self.get_preco() * 1.5 / 100
        return self.get_preco() + imposto
    
class Carrinho():
    def __init__(self):
        self.__itens = []
        self.__total = 0.0

    def adicionar_carrinho(self, nome, preco):
        self.__itens.append({"Nome": nome, "Preço": preco})
        self.__total += preco

    def remover_produto(self, nome):
        for p in self.__itens:
            if p["Nome"].lower() == nome.lower():
                self.__itens.remove(nome)
                self.__total -= p["preço"]
                break   

    def listar_produtos(self):
        if not self.__itens:
            print("Nenhum produto encontrado...")
        for p in self.__itens:
            print(f"{p["Nome"]} - Kz {p["Preço"]}")

    def calculo_total(self):
        return self.__total