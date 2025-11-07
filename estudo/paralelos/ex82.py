from os import system
system("cls")
print()

alunos = []
dados = []
media_maior = 0.0
for i in range(3):
    dados.append(str(input("Nome do aluno: ")))
    dados.append(int(input("Idade:  ")))
    dados.append(float(input("Nota 1: ")))
    dados.append(float(input("Nota 2: ")))
    dados.append(float((dados[2] + dados[3]) / 2 ))
    alunos.append(dados[:])
    dados.clear()

system("cls")
print("\033[1;36m=\033[m" * 60)
print(f"{"\033[1;35mLISTA DE ALUNOS\033[m":^70}")
print("\033[1;36m=\033[m" * 60)
print()
print(f"\033[1;35m{"Nome":<15} {"Idade":<15} {"Nota 1":<10} {"Nota 2":<10} {"Média"}\033[m")
print()
for aluno in alunos:
    print(f"\033[1;36m{aluno[0]:<15}",end=" ")
    print(f"{aluno[1]:<15}",end=" ")
    print(f"{aluno[2]:<10}",end=" ")
    print(f"{aluno[3]:<10}",end=" ")
    print(f"{aluno[4]}\033[m",end=" ")
    print()

print()
print("=-"*35)
for l in alunos:
    if media_maior == 0:
        media_maior = l[4]
    else:
        if l[4] > media_maior:
            media_maior = l[4]
            
for l in alunos:
    if l[4] > 7 and l[1] <= 20:
            print(f"\033[1;32mO {l[0]} teve {l[4]} como média e é menor de 21 anos!\033[m")

for i in alunos:
    if i[4] == media_maior:
        print(f"\033[1;32mO {i[0]} teve {i[4]} como a maior média da lista!\033[m")