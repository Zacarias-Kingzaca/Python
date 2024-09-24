from os import system
system("cls")
print("")

pessoa = {
     "nome": "Teste",
     "peso": 0.0,
     "idade": 0
}

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])

pessoa["nome"] = "Texto"
pessoa["peso"] = 99.99
pessoa["idade"] = 10

print("")

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])

print("")

pessoa["nome"] = input("Digita seu nome: ")
pessoa["peso"] = float(input("Digita seu peso: "))
pessoa["idade"] = int(input("Digita su idade: "))

print("")

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])