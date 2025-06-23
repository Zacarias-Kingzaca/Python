from os import system
system("cls")
print()
aluno = {}
media = 0
aluno["nome"] = input("Nome: ")
aluno["media"] = float(input(f"Média do aluno {aluno['nome']}: "))
if  aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"

elif 5 <=  aluno["media"] < 7:
    aluno["situacao"] = " Em recuperação"

else:
    aluno["situacao"] = "Reprovado"

print("-=-"* 30)
for k, v in aluno.items():
    print(f"- {k} é gual a {v}")

