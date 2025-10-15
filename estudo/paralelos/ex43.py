from os import system
from op import operacao
system("cls")
print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    
    def set_preco(self):
        troco = 0
        preco = float(input("Digta o valor: "))
        if self.__preco <= 0 or self.__preco > preco:
            print("Valor inválido.")
        else:
            if preco == self.__preco:
                 print("\033[1;32mCompra efetuada com sucesso.")
            elif preco > self.__preco:
                troco = preco - self.__preco
                print(f"O seu troco é {troco:.2f}kzs")

    def get_desconto(self):
        desconto = 0
        preco = 0
        desconto = (self.__preco * 10) / 100
        preco = self.__preco - desconto
        print(f"O preco com o desconto passa a ser {preco:.2f}kzs")

nome = input("Nome do produto: ")
preco = float(input("preco do produto: "))
p = Produto(nome, preco)

while True:

    print("1 Digitar o preço para comprar ")
    print("2 Mostrar preço com desconto de 10%")
    print("3 Sair")
    op = input("Escolha: ")


    if op == "1":
        system("cls")
        p.set_preco()
        operacao()

    elif op == "2":
        system("cls")
        p.get_desconto()
        operacao()

    elif op == "3":
        system("cls")
        break
