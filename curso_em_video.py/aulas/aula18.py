from os import system
system("cls")
print()

dado = list()
pessoas = list()
maior = menor = 0
for i in range(0, 3):
    dado.append(input("Digita seu nome: "))
    dado.append(int(input("Digita sua idade: ")))
    pessoas.append(dado[:])
    dado.clear()
for p in pessoas:
    if p[1] > 21:
        maior += 1
    else:
        menor += 1
print(f'Dentro desta lista tem {maior} pessoas maiores de idade, e {menor} menores de idade.')
