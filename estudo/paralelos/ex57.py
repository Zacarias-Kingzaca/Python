from os import system
system("cls")
print()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.ideda = idade


    def apresentar(self):
        print(f"Nome: {self.nome} \nIdade: {self.ideda}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade) #chama o construtor da classe pai
        self.curso = curso


    def apresentar(self):
        super().apresentar()
        print(f"Curso: {self.curso}")

a1 = Aluno("Zaca", 20, "IG")
a1.apresentar()