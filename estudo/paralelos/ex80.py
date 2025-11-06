from os import system
import csv
system("cls")
print()

#Para Ler arquivo CSV
#with open("aluno.csv", "r", newline="", encoding="UTF-8") as arquivo:
#    leitor =  csv.reader(arquivo)
#    for linha in leitor:
#       print(linha)

#Para escrever em arquivo CSV

with open("aluno.csv", "w", newline="", encoding="UTF-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([f"{"Produto":<10}" f"{"Preço":<1}"])
    escritor.writerow([f"{"Mouse":<10}" f"{50:>1}"])
    escritor.writerow([f"{"Teclado":<10}" f"{50:>1}"])
    escritor.writerow([f"{"Monitor":<10}" f"{200:<1}"])
    escritor.writerow([f"{"Leptop":<10}" f"{1500:>1}"])
    escritor.writerow([f"{"Telefone":<10}" f"{400:>1}"])

with open("aluno.csv", "r", newline="", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    print("=" * 30)
    print(f"{"LISTA DE APARELHO":^30}")
    print("=" * 30)
    for p in leitor:
        print(p)

