from os import system
system ("cls")
print()
cambio = 1000
valor = int(input("Digita um valor em USDT para ver seu cambio em kzs : "))
total = cambio * valor
print(f"{valor:.2f}USDT = {total:.2f}kzs")