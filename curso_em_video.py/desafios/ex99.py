from os import system
from time import sleep
system("cls")
print()
def maior(* num ):
    maior = 0
    print("-=-" * 15)
    print("Analisando os valores passados...")
    for valor in num:
        print(f"{valor}", end=" ", flush=True)
        sleep(0.3)
        if valor >= maior:
            maior = valor 
    print(f"Foram informados {len(num)} valores ao todo")
    print(f"O maior  valor informado foi {maior}")

          
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
