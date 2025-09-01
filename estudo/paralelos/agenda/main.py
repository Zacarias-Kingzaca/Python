from os import system
from time import sleep
from nova import nova_tarefa
system("cls")
print()

print("==================AGENDA DE TAREFA==================")

print("1 - NOVA TAREFA")
print("2 - LISTAR TAREFAS")
print("3 - APAGAR TAREFA")
print("4 - SAIR")
print()
op = input("OPÇÃO: ").strip()

while True:
    if op not in ["1", "2", "3", "4"]:
        print(f"\033[1;31m{op} não é uma opção válida.\033[m")
        op = input("OPÇÃO: ").strip()
    else:
        break
    if op == "1":
        system("cls")
        nova_tarefa()
        break