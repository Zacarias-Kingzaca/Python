from os import system
from random import randint
from time import sleep
system("cls")
print()

def sorteia(lista):
    for i in range(5):
        lista.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in lista:
        print(f'{i}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    somap = 0 
    for i in lista:
        if i % 2 == 0:
            somap += i
    print(f'Somando os valores da lista {lista}, temos {somap} ')
    

numeros = []
sorteia(numeros) 
somaPar(numeros)
