from os import system
system("cls")
print()
alunos = []
while True:
    nome = input("Nome: ").title()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1 , n2], media])
    per = input("Quer continuar [S/N]: ")
    if per in "Nn":
        break
print("=-"*32)
print(f"{"No.":<4}"  f"{"NOME":<10} {"MÉDIA":>8} ")
print("-"*30)
for i, j in enumerate(alunos):
    print(f"{i:<4}{j[0]:<10}{j[2]:>8.1f}")
print("-"*32)


while True:
    print("-"*32)
    mostra = int(input("Mostrar nota de qual aluno? (999 Interrompe): "))
    if mostra == 999:
        print("FINALIZADO")
        break
    if mostra <= len(alunos) - 1:
        print(f"Notas de {alunos[mostra][0]} são {alunos[mostra][1]}")
print("<<< Volte sempre >>>")
