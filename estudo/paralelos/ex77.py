from os import system
from abc import ABC, abstractmethod
from time import sleep
from op import operacao
system("cls")
print()


class Produtos(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def calcular_imposo(self):
        pass

    def get_nome(self):
        return self._nome
    def get_preco(self):
        return self._preco

class Eletronicos(Produtos):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def calcular_imposo(self):
        return self.get_preco + (self._preco * 10 / 100)
    
class Roupas(Produtos):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def calcular_imposo(self):
        return self.get_preco + (self._preco * 5 / 100)
    

class Alimentos(Produtos):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def calcular_imposo(self):
        return self.get_preco + (self._preco * 2 / 100)
    
class Carrinho():
    def __init__(self):
        self.lista = []
        self.total = 0

    def adicionar(self, produto):
        self.lista.append(produto)
        self.total += p.get_preco()
        print("Produto adicionado.")
   
    def remover_produto(self, nome):
        for p in self.lista:
            if p.get_nome().lower() == nome.lower():
                self.total -= p.get_preco()
                self.lista.remove(p)
                break
        else:
            print("Nenhum Produto encontrado.")

    def listar_produtos(self):
        print(f"{"Nome do produto":<10} {"Preço":>25}")
        for p in self.lista:
            print(f"{p.get_nome():<10} {p.get_preco():>32.2f} - kzs")
        
    def ver_total(self):
        print(f"O total do carrinho é kzs {self.total:.2f} - kzs")


carrinho = Carrinho()
while True:
    system("cls")
    print("1 Adicionar produto")
    print("2 Remover produto")
    print("3 Ver carrinho")
    print("4 Ver total")
    print("5 Sair")
    op = input("Escolha: ")
    
    if op == "1":
        while True:
            system("cls")
            print("1 Eletronico")
            print("2 Roupas")
            print("3 Alimento")
            op = input("Escolha: ")
            if op == "1" or op == "2" or op == "3":
                try:
                    nome = input("Nome do produto: ")
                    preco = float(input("Preço do produto: "))
                except:
                    print("Erro ao adicionar produto")
                    sleep(3)
                else:
                    if op == "1":
                        p = Eletronicos(nome, preco)
                    elif op == "2":
                        p = Roupas(nome, preco)
                    else:
                        p = Alimentos(nome, preco)
                    carrinho.adicionar(p)
                    break
            
  
    elif op == "2":
        system("cls")
        nome = input("Nome do produto: ")
        carrinho.remover_produto(nome)
        operacao()

    elif op == "3":
        system("cls")
        carrinho.listar_produtos()
        operacao()

    elif op == "4":
        system("cls")
        carrinho.ver_total()
        operacao()

    elif op == "5":
        system("cls")
        break

    else:
        system("cls")
        print("Opção inválida.")
        operacao()
    
        