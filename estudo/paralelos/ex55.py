from os import system
system("cls")
print("")

dado = []
pessoas = []
while True:
    dado.append(input("Nome: ").title())
    dado.append(int(input("Idade: ")))
    dado.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    res = input("Quer continuar [S/N]: ")
    if res[0] in "nN":
        break
system("cls")
for p in pessoas:
    print(f'Nome: {p[0]}')
    print(f'Idade: {p[1]} de idade')
    print(f'Peso: {p[2]} kg')
    print("==================================")



if p[1] == maior:
        print("", end="")
print(f"A maior idade registrada é {maior} anos de idade. Idade de ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{[p[0]]}", end='')
print()
if p[1] == menor:
        print("", end=" ")
print(f"A menor idade registrada é {menor} anos de idade. Idade de ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"{[p[0]]}", end=' ')
