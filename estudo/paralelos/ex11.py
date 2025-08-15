from os import system
system("cls")
print

arquivo = open ("C:/kingzaca/vs code/Python/estudo/paralelos/mensagem.txt", "r")
linhas = arquivo.readlines()
for linha in linhas:
    print(linha)   