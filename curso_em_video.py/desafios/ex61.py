from os import system
system("cls")
print()
print("GERADOR DE PA")
print(10*"-=-")
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end="")
    termo += razao
    cont += 1
print("FIM")