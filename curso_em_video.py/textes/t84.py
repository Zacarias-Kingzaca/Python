from os import system
system("cls")
print()

print("="*50)
print("{:^50}".format("MÉDIA DE TEMPERATURA"))
print("="*50)

d1 = int (input("Digita a temperatura da segunda feira: "))
d2 = int (input("Digita a temperatura da terça feira: "))
d3 = int (input("Digita a temperatura da quarta feira: "))
d4 = int (input("Digita a temperatura da quinta feira: "))
d5 = int (input("Digita a temperatura da sexta feira: "))
d6 = int (input("Digita a temperatura do sabádo: "))
d7 = int (input("Digita a temperatura do domingo: "))

media = (d1 + d2+ d3+ d4+ d5+ d6+ d7) / 7
print(f"A média da temperatura semanal foi de {media:.2f}º")




