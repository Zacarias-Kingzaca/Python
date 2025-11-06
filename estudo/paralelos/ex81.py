from os import system
import csv
system("cls")
print()


with open("aluno.csv","w", newline="", encoding="utf-8") as f:
    arquivo = csv.writer(f)
    arquivo.writerow([f"{"Nome":<25}" f"{"Idade":<2}"]) 
    for i in range(1, 4):
        nome =  input(f"Nome do {i}ª aluno: ")
        idade = int(input(f"Idade do {i}ª aluno: ")) 
        arquivo.writerow([f"{nome:<25}" f"{idade:<2}"]) 
    

system("cls")
with open("aluno.csv", "r", newline="", encoding="utf-8") as f:
    print("=" * 50)
    print(f"{"LISTA DE ALUNOS":^50}")
    print("=" * 50)
    arquivo = csv.reader(f)
    for i in arquivo:
        print(i)
