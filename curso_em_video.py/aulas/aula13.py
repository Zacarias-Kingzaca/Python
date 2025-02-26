from os import system
system("cls")
print()

s = 0
for c in range(0, 4):
    n = int(input("Digita umm valor: "))
    s += n
print("O somatório de todos os números foi {}".format(s))