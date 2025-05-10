from os import system
system("cls")
print()

for i in range(5):
    peso = float(input(f" {i}º Pessoa digita o seu peso: ")) 
    altura = float(input(f" {i}º Pessoa digita a sua altura: ")) 
    i+1
    imc = peso / altura**2
    pessoa += i
print(pessoa)