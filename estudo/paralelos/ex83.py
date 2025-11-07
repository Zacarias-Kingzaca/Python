from os import system
system("cls")
print()

produtos = [

            ["Ma[==use", 50],
            ["Teclado", 80],
            ["Monitor", 600]
]
for p in produtos:
    p[1] += p[1] * 10 / 100
for p in produtos:
    print(f"{p[0]}  - kzs {p[1]}", end=" ")
    print()

produt = input("Digita o nome do produto que Você deja: ").lower()
for p in produtos:
    if p[0].lower() == produt:
       print(f"Produto encontrado está custando - kzs {p[1]}") 
       break
else:
    print("Produto não encontrado.")
