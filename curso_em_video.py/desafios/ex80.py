from  os import system
system("cls")
print("")
lista = [] 
for i in range(0, 5):
    n = int(input("Digita um valor: "))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print("Foi adicionado no final da lista.")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
             lista.insert(pos, n)
             print(f"Foi adicionado na posição {pos}.")
             break
            pos += 1 
print(".=."*30)
print(f"Os valores digitados em ordem são {lista}")