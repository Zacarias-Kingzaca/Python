from os import system
from time import sleep
from random import (randint)
from operator import itemgetter
system("cls")
print()

jogo  = {"jogador1": randint(1, 6),
         "jogador2": randint(1,6),
         "jogador3": randint(1, 6),
         "jogador4": randint(1, 4)}

ranking = list()
print("Valores sorteados: ")
for k, v in jogo.items():
    print(f"{k} jogou {v} no dado")
    sleep(1)
print("-=-"*10)
print("== RANKING DOS JOGADORES == ")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i + 1}º lugar: {v[0]} com {v[1]} ")
    sleep(1)

