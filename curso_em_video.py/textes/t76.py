from os import system
system("cls")
print()

n1 = int(input("Digita a primeira nota: "))
n2 = int(input("Digita a segunda nota: "))
n3 = int(input("Digita a terceira nota: "))
print()
p1 = float(input("Dita o primeiro peso: "))
p2 = float(input("Digita o segundo peso: "))
p3 = float(input("Digita o terceiro peso: "))

media_p = (n1 + p1) + (n2 + p2) + (n3 + p3) / p1 + p2 + p3
print()

print(f"A média ponderada será {media_p}")
