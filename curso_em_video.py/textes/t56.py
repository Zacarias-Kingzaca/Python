from os import system
system("cls")
print()

print("=========================")
print("{:^25}".format("LOJA ZACARIAS"))
print("=========================")
somap =  mediap = produto = 0
for i in range(1,6):
    preco = float(input(f"Digita o preço do {i}º produto kzs: "))
    somap += preco
    produto += 1
mediap = somap / produto
print(f"O valor da soma de todos os produtos é {somap:.2f}kzs")
print(f"A média entre eles é de {mediap:.2f}kzs")