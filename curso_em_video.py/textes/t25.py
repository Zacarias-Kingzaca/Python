from os import system
system("cls")
print()

temperatura = int(input("Qual é a teperatura atual? "))

if temperatura < 20:
    print(f"O clima está frio com a teperatura de {temperatura}ºC")
elif temperatura > 20 and temperatura < 30:
    print(f"O clima está moderado com a temperatura de {temperatura}ºC")
else:
    print(f"O clima está quente com a temperatura de {temperatura}ºC")