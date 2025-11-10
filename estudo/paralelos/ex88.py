from os import system
import csv
system("cls")
print()

with open("aluno.csv", "w", newline='', encoding="UTF-8") as a:
   arquivo = csv.writer(a)
   arquivo.writerow([[f"{"Nome":<12} {"Idade":<15} {"Nota"} {"Média":>15} "]])
   arquivo.writerow([[f"{"Zacarias":<12}  {"19":<8}"],  [10.0, 10.0],     [(10.0 + 10.0) / 2]])
   arquivo.writerow([[f"{"Pedro":<12}  {"18":<8}"],     [10.0, 4.0],      [(10.0 + 4.0) / 2]])
   arquivo.writerow([[f"{"Ana":<12}  {"20":<8}"],       [10.0, 3.0],      [(10.0 + 3.0) / 2]])
   arquivo.writerow([[f"{"Luisa":<12}  {"17":<8}"],     [10.0, 5.0] ,     [(10.0 + 5.0) / 2]])

with open("aluno.csv", "r", encoding="utf-8") as f:
    arquivo = csv.reader(f)
    print("=" * 62)
    print(f"{"LISTA DE APARELHO":^62}")
    print("=" * 62)
    for p in arquivo:
        print(p)


