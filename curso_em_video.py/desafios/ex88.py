from os import system
from random import randint
from time import sleep
system("cls")
print()

print("="*30)
print("{:^30}".format("JOGO de MEGA SENA"))
print("="*30)
lista = []
jogos = []        
tot = 1
vezes = int(input("Qauntos palpites quer gerar: "))

while tot <= vezes:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("-=-"*3, f"\033[1;32mSORTEANDO {vezes} JOGOS\033[m", "-=-"*3)
for i, l in enumerate(jogos):
 sleep(1)
 print(f"Jogo {i+1}: {l}")
print("-=-"*3, " < BOA SORTE >", "-=-"*3)
