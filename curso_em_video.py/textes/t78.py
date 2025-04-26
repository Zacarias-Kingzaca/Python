from os import system
system("cls")
print()

custo = float(input("Digita o custo do produto kzs: "))
preco = float(input("Digita o preço do produto kzs: "))

if custo > preco:
    print("Negócio feito com prejuízo.")
elif custo < preco:
    print("Negócio feito com lucro.")
else:
    print("Negócio sem perda nem ganho.")