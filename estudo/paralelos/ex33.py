from os import system
system("cls")
print()

turma_a = ["Ana", "Bruno", "Carlos"]
turma_b = ["Diana", "Bruno", "Eduardo"]
turma_c = []

for nome in turma_a:
    turma_c.append(nome)
for nome in turma_b:
    turma_c.append(nome)

turma_c = list(set(turma_c))
print(sorted(turma_c))