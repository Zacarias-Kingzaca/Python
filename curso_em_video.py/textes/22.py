from os import system
import math
from turtle import *
system("cls")
print()

def hearta(k):
    return 15*math.sin(k)**3
def hearbt(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed (0)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20, hearbt(i)*20)
    for j in range(5):
        color("red")
    goto(0, 0)
done( )