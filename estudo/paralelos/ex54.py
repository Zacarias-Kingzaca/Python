from os import system
system("cls")
print()

dado = list()
galera = list()

while True:
    dado.append(input("Nome: ").title())
    dado.append(float(input("Peso: ").strip()))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if    dado[1] < menor:
            menor = dado[1]
    res = input("Quer continuar [N/S]: ").upper()
    galera.append(dado[:])
    dado.clear()
    if res[0] in "S":
        continue
    elif res[0] in "N":
        break
    else:
        while True:
            print("Escolha errada.")
            res = input("Quer continuar [N/S]: ").upper()
            if res[0] in "S":
               break
            elif res[0] in "N":
                exit()
            else:
                continue
print("=-"*50)
print(f"Ao todo, você cadastrou {len(galera)} pessoas.")
print(f"O maior peso foi de {maior}kg. Peso de ", end="")
for p in galera:
    if p[1] == maior:
        print(f"{[p[0]]}", end="")
print()
print(f"O menor peso foi de {menor}kg. Peso de ", end="")
for p in galera:
    if p[1] == menor:
        print(f"{[p[0]]}", end="")