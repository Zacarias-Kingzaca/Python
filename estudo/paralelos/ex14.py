from os import system
system("cls")
print()
cont = pal = 0
with open("dados.txt","r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        pal += len(linha.split()) 
        cont += 1
        
print(f"Este arquivo que acabou de ler tem {cont} linha(s) e {pal} palavra(s)")
