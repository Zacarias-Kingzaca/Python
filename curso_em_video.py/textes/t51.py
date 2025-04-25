from os import system
from time import sleep
from random import randint
system("cls")
print()
print(30*"=")
print("{:^30}".format("JOGO DE DADOS"))
print(30*"=")

print("DADOS GIRANDO")
dados1 = randint(1,6)
sleep(2)
print(dados1)
print("------------")
print("DADOS GIRANDO")
dados2 = randint(1,6)
sleep(2)
print(dados2)
print("------------")
print(f"{dados1} + {dados2} = {dados1+dados2}")
