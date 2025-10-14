from os import system
from op import operacao
system("cls")
print()

class Passageiro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Viagem:
    def __init__(self, destino):
        self.destino = destino
        self.passageiro = []

    def adicionar_passageiro(self, pessoa):
        self.passageiro.append(pessoa)


    def listar_passageiro(self):
        try:
            for p in self.passageiro:
                print(f"Nome do passageiro: {p.nome} ")
                print(f"Idade: {p.idade} anos")
                print(f"Destino: {self.destino}")
                print("========================================================")
        except:
            print("Nenhum passageiro encontrado.")

    def verificar_maior_de_idade(self):
        try:
            for p in self.passageiro:
                if p.idade > 17:
                    print(f"Nome do passageiro: {p.nome}")
                    print(f"Idade: {p.idade} anos")
                    print(f"{self.destino}")
                    print("========================================================")
        except:
            print("Nenhum passageiro encontrado.")


destino = input("Destino da viagem: ")
viagem = Viagem(destino=destino)

while True:
    print("1 - Adicionar Passageiro: ")
    print("2 - Listar passageiros")
    print("3 - Verificar maiores de idade")
    print("4 - Sair")    
    op = input("Escolha: ")

    if op == "1":
        system("cls")
        nome = input("Nome do passageiro: ").title()
        idade = int(input("Idade: ").strip())    
        p = Passageiro(nome, idade)
        viagem.adicionar_passageiro(p)
        operacao()

    elif op == "2":
        system("cls")
        viagem.listar_passageiro()
        operacao()

    elif op == "3":
        system("cls")
        viagem.verificar_maior_de_idade()
        operacao()

    elif op == "4":
        system("cls")
        break

    else:
        print("Opção inválida.")