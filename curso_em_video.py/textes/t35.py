from os import system
system("cls")
print()

temperatura = int(input("Digita a temperatura atual: "))
f = temperatura * 9/5 + 32
print(f"A temperatura de {temperatura}ºC convertido em Farhrenheit é de {f}farhrenheit")