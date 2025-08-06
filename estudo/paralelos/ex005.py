from os import system
system("cls")
print()

def  tarefas(*tarefa, propriedade="Alta"):
    tarefa = list(set(tarefa))
    tarefa = [p.capitalize() for p in tarefa]
    filtrada = [t for t in tarefa if t.startswith(propriedade[0]) ]
    print(f"Você tem {len(filtrada)} tarefas com propriedade {propriedade}")


tarefas("alta Lavar ", "alta fazer compras", "alta arrumar", "dormir")