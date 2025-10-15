from os import system
from op import operacao
system("cls")
print()


class Pessoa:
    def __init__(self, nome,idade):
        self.__nome = nome
        self.__idade = idade


    def ser_alterar_idade(self, idade):
        if self.__idade < idade:
            self.__idade = idade
        else:
            return "Erro impossível realizar tarefa."
        
    def get_mostrar_idade(self):
        if self.__idade:
            return self.__idade
        return 0
    
        
pessoa = Pessoa("Zaca", 17)
pessoa.ser_alterar_idade(18)
print(pessoa.get_mostrar_idade())
