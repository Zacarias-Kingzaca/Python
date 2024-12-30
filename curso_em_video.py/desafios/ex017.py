from os import system
system("cls")
print()

ca = float(input("Digita o valor do cateto oposto : "))
co = float(input("Digita o valor do cateto adjacente : "))

ipo = (ca * 2 + co * 2)

print("O comprimento da Hipotenusa é {:.2f}".format(ipo))