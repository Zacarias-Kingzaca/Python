from os import system
system("cls")
print()

while True:
    try:
        n = int(input("Digita um valor: "))
    except ValueError:
        print("\033[1;31mPor favor digita um número inteiro.\033[m")
    else:
        print(f"\033[1;32mO dobro do número {n} é {n*2}\033[m")
        break
    finally:
        print("Programa finalizado com sucesso.")
        

