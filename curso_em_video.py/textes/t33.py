from os import system
system("cls")
print()
c_medio = 0
distancia = int(input("Digita a distância percorrida na viagem (Kmh): "))
consumo = int(input("Digita o consumo de combustível em (L): "))
c_medio = distancia / consumo
print(f"O consumo médio de combustível na viagem foi de {c_medio:.0f}L")