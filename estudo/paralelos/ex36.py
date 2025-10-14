from os import system
from op import operacao
system("cls")
print("")

class Contato:
    def __init__(self, nome, numero, email):
        self.nome = nome
        self.numero = numero
        self.email = email


class Agenda:
    def __init__(self):
        self.lista = []

    
    def adicionar_contato(self, contato):
        self.lista.append(contato)
        print("Contato adicionado com sucesso!")

    def buscar_por_nome(self, nome):
        encontrou = False
        for n in self.lista:
            if n.nome.lower() == nome.lower():
                print(f"Nome: {n.nome}\nNúmero: {n.numero}\nE-mail: {n.email}")
                encontrou = True
        if not encontrou:
            print("Nome não encontrado.")

    def remover_contato(self, num):
        encontrou = False
        for n in self.lista:
            if n.numero == num:
                self.lista.remove(n)
                encontrou = True
                print("Número deletado com sucesso!")
        if not encontrou:
            print("Número não encontrado.")

cont = Agenda()

while True:
    print("1 - Adicionar contato")
    print("2 - Buscar por nome")
    print("3 - Apagar contato")
    print("4 - Sair ")
    op = input("Escolha: ")

    if op == "1":
        system("cls")
        nome = input("Nome: ")
        numero = (input("Número: ").strip())
        email =  input("E-mail: ")
        c = Contato(nome, numero, email)
        cont.adicionar_contato(c)
        operacao()

    elif op == "2":
        system("cls")
        nome = input("Nome: ")
        cont.buscar_por_nome(nome)
        operacao()

    elif op == "3":
        system("cls")
        n = input("Número: ").strip()
        cont.remover_contato(n)
        operacao()

    elif op == "4":
        system("cls")
        break
    else:
        print("Escolha errada")
        print("")