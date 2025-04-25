from os import system
from random import randint 
system("cls")
print()

print(50*"=")
print("{:^50}".format("JOGO DE CARA OU COROA"))
print(50*"=")
computador = randint(1,2)
print("---------------------ESCOLHA----------------------")
print("""
        [1] CARA
        [2] COROA 
      """)
usuario = int(input("CARA OU COROA [1/2]: "))
if computador == usuario:
    print("Jogador você Venceu!")
else:
    print("Jogador você perdeu!")

