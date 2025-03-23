from os import system
system("cls")
print()  
while True:
    n = int(input("Quer ver a tabuada de que valor: "))
    print(30*"-")
    if n < 0:
        break
    for c in range(1, 13):
     print(f"{n} X {c} = {n*c}")
     print(30*"-")
print("PROGRAMA DE TABUADA ENCERRADO!")
     