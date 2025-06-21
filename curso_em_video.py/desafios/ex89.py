from os import system
system("cls")
print("")
alunos = []
while True:
    nome = (input("Nome: "))
    nota1 = (float(input("Nota 1: ")))
    nota2 = (float(input("Nota 2: ")))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    res = input("Quer continuar [S/N]: ")
    if res in "Nn":
        break
print("-=-"*30)
print(f"{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-"*26)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print("-" * 35)
    opc = int(input("Mostrar nota de qual aluno? (999 interrompe): "))
    if opc == 999:
        from time import sleep
        sleep(1)
        print("FINALIZANDO...")
        break
    if opc <=  len(alunos) - 1:
        print(f"Nota de {alunos[opc][0]} são {alunos[opc][1]}")
print("<<< VOLTE SEMPRE >>>")
