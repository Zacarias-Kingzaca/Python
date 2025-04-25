from os import system
from  time import sleep
from random import randint
system("cls")
print()

print(50*"=")
print("{:^50}".format("SORTEIO"))
print(50*"=")

print("SORTEANDO UM NÚMERO DE 1 A 60:")
sleep(2)
comp = randint(1,60)
print("Sorteando...")
sleep(2)
print(comp)