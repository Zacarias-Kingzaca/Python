from os import system
system("cls")
print()

print("-"*40)
print("Sequencia de Fibonacci")
print("-"*20)
n = int(input("Quantos termos você quer gerar: "))
t1 = 0
t2 = 1
print("-"*40)
print("{} -> {}".format(t1, t2), end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print("-> {}".format(t3),end="")
    t1 = t2
    t2 = t3
    cont += 1
print("-> FIM")
print("-"*40)