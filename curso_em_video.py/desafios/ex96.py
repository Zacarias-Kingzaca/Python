from os import system
system("cls")
print()

def área(larg, compr):
    resultado = larg * compr
    print(f"A area de um terno de {larg} por {compr} é de {resultado} m quadrado")

  
print("Controle de Terrenos")
print("--------------------")  
l = int(input("LARGURA (m): "))
c = float(input("COMPRIMENTO: "))
área(l, c)
