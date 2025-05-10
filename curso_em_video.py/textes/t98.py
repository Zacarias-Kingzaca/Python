from os import system
system("cls")
print()

atual = float(input("Digita o seu peso atual: "))
meta = float(input("Digita a sua meta que desejas alcansar: "))

if atual > meta:
    peso = atual - meta
    print(f"Você precisa perder {peso}kg para alcansar os {meta}kg")
else:
    peso = meta - atual
    print(f"Você precisa ganhar mais {peso}kg para alcansar os {meta}kg")