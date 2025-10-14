from os import system
from op import operacao
system("cls")
print()

class Tarefa:
    def __init__(self, nome, prioridade, concluida):
        self.nome = nome
        self.prioridade = prioridade
        self.concluida = concluida


class ListaDEtarefas:
    def __init__(self):
        self.tarefas = []

    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_pendentes(self):
        encontrou = False
        for i in self.tarefas:
            if i.concluida == False:
                encontrou = True
                print(f"{i.nome}: {i.concluida}")
        if not encontrou:
            print("Nenhuma tarefa encontrada")

    
    def concluir_tarefa(self, nome):
        encontrou = False
        for i in self.tarefas:
            if i.nome.lower() == nome.lower():
                encontrou = True
                if i.concluida == False:
                    i.concluida = True
                    print("Tarefa concluida!")
                elif i.concluida == True:
                    print("A tarefa já foi concluida!")
        if not encontrou:
            print("Nenhuma tarefa encontrada")


tarefas = ListaDEtarefas()
while True:
    print("1- Adicionar Tarefa")
    print("2- Listar tarefas pendentes")
    print("3- Concluir tarefas")
    op = input("OP: ")

    if op == "1":
        system("cls")
        nome = input("Nome da tarefa: ").strip().title()
        prioridade = int(input("Digita consuante o nível de prioridade: [1, 2, 3]: ").strip())
        concluido = int(input("Escolhe 1 para tarefa realizada ou qualquer outro número para não realizada:  "))
        if concluido == 1:
            concluido = True
        else:
            concluido = False
        t = Tarefa(nome, prioridade, concluido)
        tarefas.adicionar_tarefa(t)
        operacao()

    elif op == "2":
        system("cls")
        tarefas.listar_pendentes()
        operacao()

    elif op == "3":
        system("cls")
        nome = input("Nome: ").strip().title()
        tarefas.concluir_tarefa(nome)
        operacao()

    elif op == "4":
        system("cls")
        break
    
    else:
        print("Operação errada!")
