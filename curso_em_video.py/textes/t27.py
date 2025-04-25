from os import system
system("cls")
print()
soma = media = 0
for i in range(1, 4):
    n = int(input(f"digita o {i}ª valor:  "))
    soma += n
media =  soma / 3
print(f"Aluno aprovado com a média {media:.0f}" if media >= 7 else f"Aluno reprovado com a media {media:.0f}" )