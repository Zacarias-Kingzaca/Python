from os import system
system("cls")
print()

print("GERADOR DE PA")
print(10*"-=")
primeioro = int(input("Primeiro termo: "))
razao = int(input("digite a razão: "))
termo = primeioro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais 
    while cont <= total:
        print("{} -> ".format(termo), end='')
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar mais? "))
print("Progrssão finalizada com {} termos mostrados".format(total))

