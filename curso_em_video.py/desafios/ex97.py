from os import system
system("cls")
print()
 
def escreva(msg):
    tam = len(msg) + 4
    print("^" * tam )
    print(f"  {msg}")
    print("^" * tam )


escreva("Zacarias Eduardo João")
escreva("Zacarias King Zaca")
escreva("King Zaca")