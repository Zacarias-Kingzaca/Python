from os import system
from random import randint
from time import sleep
from operator import itemgetter
system("cls")
print()

jogador = {
    "Jogador1": randint(1, 6),
    "Jogador2": randint(1, 6),
    "Jogador3": randint(1, 6),
    "Jogador4": randint(1, 6)
 }

for k, v in jogador.items():
    print(f"Jogador {k} tirou {v} no dado.")
    sleep(2)
nova = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print("-=" * 30)
print("== RANKING DOS JOGADORES ==")
for k, v in enumerate(nova):
    print(f" {k + 1 }º Lugar:  {v[0]} com {v[1]}")
print(nova[2])

