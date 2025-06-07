from os import system
system("cls")
print()

comida = "Arroz", 2000, "Fuba", 200, "Peixe", 40, "Trigo", 500, "Oléo", 100, "Açucar", 60, "Frango", 200, "Carne", 300, "Ovo", 400, "Leite", 10,"Massa" , 20
print(50*"-")  
print(f"{"Lista de compra":^50}")
print(50*"-")

for c in range(len(comida)):
    if c % 2 == 0:
        print(f"{comida[c]:.<30}kzs", end=" ")
    else:
        print(f"{comida[c]:>10.2f}")