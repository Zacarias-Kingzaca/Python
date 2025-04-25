from os import system
from time import sleep
system("cls")
print()
print(27*"\033[1;35m=\033[m")
print("{:^32}".format("\033[1mLOGIN\033[m"))
print(27*"\033[1;35m=\033[m")
print()
senha = str(input("\033[1mDigita a sua senha: \033[m"))
print("\033[1;36mVerificando...\033[m")
sleep(1)
print("\033[1;36mAutenticando...\033[m")
sleep(1)
print("\033[1;32mSEJA BEM-VINDO\033[m" if senha == "Zaca01234" else "\033[1;31mSENHA INCORRETA\033[m")