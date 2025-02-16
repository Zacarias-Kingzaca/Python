from os import system
from random import randint
from time import sleep
system ("cls")
print()

itens = ("PEDRA" , "PAPEL", "TESOURA")
computador = randint(0,2)
print()
print("""SUAS OPÇÕES: 
      
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA
      """)
print()
jogador = int(input("ESCOLHA A SUA OPÇÃO JOGADOR: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-=-"*10)
print("Computador jogou: {}".format(itens[computador]))
print("Jogador jogou: {}".format(itens[jogador]))
print("-=-"*10)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIADA!")
elif computador == 1: #computador jogou PAPEL
    if jogador ==  0:
        print("COMPUTDOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIADA!")
elif computador == 2: #computador jogou TESOURA
    if jogador ==  0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIADA!")

