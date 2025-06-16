from os import system
system("cls")
print()

dados = []
pessoas = []
maior = 0
menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('peso: ')))
    if len(dados) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    res = input('Quer continuar [S/N]: ')
    if res in "Nn":
        break
print(50*"=")
print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maior}kg. Peso de", end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f"O menor peso foi de {menor}kg. Peso de", end=" ")
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()