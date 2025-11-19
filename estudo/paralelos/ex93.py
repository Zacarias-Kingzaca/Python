from os import system
import csv
system("cls")
print()


with open("fixa.csv", "w", newline="", encoding="UTF-8") as f:
    arquivo = csv.writer(f)
    arquivo.writerow([[f"{"Nome":<10} {"Preço":<10}"]])
    arquivo.writerow([[f"{"peixe":<10} {200:>10.2f}"]])
        
with open("fixa.csv", "r", encoding="utf-8") as f:
    arquivo = csv.reader(f)
    print("=" * 62)
    print(f"{"LISTA DE PRODUTOS":^62}")
    print("=" * 62)
    for p in arquivo:
        print(p)