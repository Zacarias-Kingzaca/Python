from os import system
from op import operacao
system("cls")
print()

class Aluno:
    def __init__(self, nome, notas):
        self.__nome = nome
        self.__notas = notas

    def calcular_media(self):
        if self.__notas:
          return sum(self.__notas) / len(self.__notas)
        return 0
    

    def Situacao(self):
        if self.__notas:
            if sum(self.__notas) / len(self.__notas) > 7:
                return "Aprovado"
            else:
                return "Reprovado"
        else:
            return "Erro"

a = Aluno('zacarias', [10, 9, 10])
print(f"{a.calcular_media():.1f}")
print(a.Situacao())
