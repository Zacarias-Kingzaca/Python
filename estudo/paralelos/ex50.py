from os import system
system("cls")
print()
lista = []
for i in range(1, 4):
    nome = input(f"Nome do {i}ª aluno: ").title()
    nota = float(input(f"Nota do {i}ª aluno: ").strip())
    lista.append([nome, nota])
system("cls")
print("="*30)
print("Nome e nota dos alunos")
print("="*30)
for alunos in lista:
    print(f"Nome: {alunos[0]}")
    print(f"Nota: {alunos[1]}")
    print("==============================")
print()
print("Alunos com nota maior que 6")
for alunos in lista:
    if alunos[1] >= 7:
        print(f"Nome: {alunos[0]}")
        print(f"Nota: {alunos[1]}")
        print("==============================")  