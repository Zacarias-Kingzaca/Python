from os import system
system("cls")
print()
soma = media = 0
for i in range(1,5):
    n = float(input(f"Digita a  {i}ª nota: "))
    soma += n
media = soma / 4 
if media >= 6:
    print("Aluno apto!")
else:
    print("Aluno não apto!")