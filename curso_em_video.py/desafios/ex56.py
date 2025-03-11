from os import system
system("cls")
print()
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher = 0
for p in range(1, 5):
    print("===== {}ª Pessoa =====".format(p))
    nome =  str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]:")).strip()
    print()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Fm" and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mas velho tem {} anos e se chama {}. ".format(idade, nome))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher))
    