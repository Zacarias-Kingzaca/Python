from os import system
system("cls")
print()

class Usuario:
    def __init__(self, Username, senha):
        self.__username = Username
        self.__senha = senha


    def set_alterar_senha(self, senha):
        if self.__senha == senha.lower().strip():
            self.__senha = input("Nova senha: ")
            print("Senha alterada.")
        else:
            print("Senha errada.")

    def get_mostrar(self):
        print(f"Nome: {self.__username}")
        print(f"Senha: {self.__senha}")

user = Usuario("Zacarias", "1234abc".lower().strip())
user.set_alterar_senha("1234abc")
user.get_mostrar()