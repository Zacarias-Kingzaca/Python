from os import system
system("cls")
print()

jogador = {}
lista = []
jogador["nome"] = input("Nome do jogador: ")
partidas = int(input("Quantas partidas ele jogou: "))
for i in range(partidas):
    lista.append(int(input(f"\tQuantas golos na partida {i}? ")))
jogador["gols"] = lista
jogador["total"] = sum(lista)
print("=-"*50)
print(jogador)
print("=-"*50)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("=-"*50)
print(f"O jogador {jogador["nome"]} jogou {partidas} partidas.")
for p in range(partidas):
    print(f"\t => Na partida {p}, fez {lista[p]} gols.")



