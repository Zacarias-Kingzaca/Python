from os import system
system("cls")
print()
r = ""
n = cont = soma = media = maior = menor = 0 
while r != "N":
    n = int(input("Digita um número: "))
    r = str(input("Quer continuar? [S/N] ")).strip().upper()
    soma += n
    cont += 1
    if cont == 1:
       maior = menor = n
    else:
        if n > maior:
          maior = n
        if n < menor:
           menor = n
    media = soma / cont
print("Você digitou {} números  e a media foi {}".format(cont, media))
print("O maior valor digitado foi {} e o menor foi {}".format(maior, menor))
