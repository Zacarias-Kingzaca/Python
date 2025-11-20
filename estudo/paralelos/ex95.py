from os import system
system("cls")
print()

aluno = {}

aluno["nome"] = str(input("Nome do aluno: ").title())
aluno["média"] = float(input("Média do aluno: "))
if aluno["média"] >= 7:
    aluno["situação"] = "Aprovado"
else:
    aluno["situação"] = "Reprovado"

for k,v  in aluno.items():
    print(f"{k} é igual a {v}")