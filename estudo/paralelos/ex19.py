from os import system
from op import operacao
system("cls")
print()
tarefas = []

def addtarefa(lista):
    print("=======================Adicionar tarefa=======================")
    titulo = input("Titulo: ")
    descricao = input("Descrição: ")
    tarefa = {"Titulo": titulo, "Descrição": descricao, "Status": "pendente"}
    lista.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    

def listar_tarefas(tarefas,status=None):
    print("=======================Adicionar tarefa=======================")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    else:
      for i , tarefa in enumerate(tarefas, start=1):     
        if status is None or tarefa["Status"] == status:
            print(f"{i}. Título: {tarefa["Titulo"]}")
            print(f"     Descrição: {tarefa["Descrição"]}")
            print(f"     Status: {tarefa["Status"]}")
            print("="*30)
    

while True:
    print("=======================Menu=======================")
    print(" 1 Adicionar tarefa")
    print(" 2 Listar tarefa")
    print(" 3 Listar tarefas pendente")
    print(" 4 Marcar tarefa como concluída")
    print(" 5 Apagar tarefa")
    print(" 6 Sair")

    op = input("-: ")
    if op not in ["1", "2", "3", "4", "5", "6"]:
        print("op não reconhecida")
    if op == "1":
        system("cls")
        addtarefa(tarefas)
        operacao()
    if op == "2":
        system("cls")
        listar_tarefas(tarefas)
        operacao()
    if op == "3":
        print
    if op == "4":
        break