from os import system
system("cls")
print("")

Palavras = []
while True:

 palavra = input ("Digite uma  palavra ou 'exit' para sair:  ")

 if palavra == "exit":
   break
 Palavras.append(palavra)

resultado = ' ' .join(Palavras)
print("Resultado da concatenação: ", resultado)