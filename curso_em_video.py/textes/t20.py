from os import system
system("cls")
print()

print("======CONTROLE DE EEIÇÕES======")

eleitor = int(input("Quantos anos tu tens? "))

if eleitor > 16:
    print("\033[1;32mParabéns estás apto para votar.\033[m")
else:
    print("\033[1;31mTu não podes votar não tens idade suficiente.\033[m")