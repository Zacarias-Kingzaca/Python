from os import system
from random import randint
system("cls")
print()

jogador = {}
gols = []
lista = []
while True:
    gols.clear()
    jogador.clear()
    jogador["nome"] = input("Nome do jogador: ")
    partidas = int(input("Quantas partidas ele jogou: "))
    for i in range(partidas):
        gols.append(int(input(f"\tQuantas golos na partida {i}? ")))
    jogador["gols"] = gols.copy()
    jogador["total"] = sum(gols)
    lista.append(jogador.copy())
    per = input("Quer continuar [S/N]: ").upper()[0]
    if per in "Ss":
        pass
    elif per in "Nn":
        break
    else:
        while True:
            print("Digita apenas [S/N].")
            per = input("Quer continuar [S/N]: ")
            if per in "Ss":
                break
            elif per in "Nn":
                stop = True
                break
print("=-"*40)
print('cod', end=" ")
for i in jogador.keys():
        print(f"{i:<15}", end=" ")
print()
print("-"*45)
for k,v in enumerate(lista):
    print(f"{k:<3}", end=" ")
    for i,j in v.items():
        print(f"{str(j):<15}", end=" ")
    print()
print("-"*45)

while True:
    mostrar = int(input("Mostrar dados de que jogador (999 para parar): "))
    if mostrar == 999:
        break
    if mostrar >= len(lista):
        print("Não existe um jogador com essse número.")
    else:
        print(f"LEVANTAMENTO DO JOGADOR {lista[mostrar]["nome"]}")
        for i, g in enumerate(lista[mostrar]["gols"]):
            print(f"    no jogo {i + 1} fez {g} gols.")
    print("-"*40)
print("<< VOLTE SEMPRE >>")