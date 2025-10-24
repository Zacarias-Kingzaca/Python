from os import system
system("cls")
print()

lista = list()
pessoas = list()

for i in range(3):
    lista.append(input(("Nome: ")))
    lista.append(int(input("Idade: ")))
    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
print("=-"*30)
print(f"Ao todo você cadastrou {len(pessoas)} pessoas")

for p in pessoas:
    p[1] == maior
    print("", end="")
print(f"A maior idade registrada foi {maior} anos de idade. Idade de ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{[p[0]]}", end=" ")
print()
for p in pessoas:
    p[1] == menor
    print("", end="")
print(f"A menor idade registrada foi {menor} anos de idade. Idade de ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"{[p[0]]}", end=" ")
   