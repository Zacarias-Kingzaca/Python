from os import system
system("cls")
print()

valores = []
for cont in range(0, 5):
    valores.append(int(input("Digita um valor: ")))

for c, v in enumerate(valores):
    print(f"na posição {c} encontrei o valor {v}!")
print("Cheguei ao fial da lista...")