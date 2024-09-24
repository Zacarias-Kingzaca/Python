from os import system
system("cls")
print("")

lista_pessoa = []

for _ in range(3):
    pessoa = {}
    pessoa["nome"] = input("Digita seu nome: ")
    pessoa["peso"] = float(input("Digita seu peso: "))
    pessoa["idade"] = int(input("Digita su idade: "))
    lista_pessoa.append(pessoa)

print("Dados das pessoas: ")
for pessoa in lista_pessoa:
    print()
    print("Nome:", pessoa["nome"])
    print("Peso:", pessoa["peso"])
    print("Idade:", pessoa["idade"])
    print()
