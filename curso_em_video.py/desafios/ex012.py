from os import system
system ("cls")
print()

preco = float(input("Qual é o preço do produto? Kzs "))
novo = preco - (preco  * 5 / 100)

print()
print("O produto que custava Kzs{:.2f}, na promoção com desconto de 5% vai custar Kzs{:.2f}".format(preco,novo))