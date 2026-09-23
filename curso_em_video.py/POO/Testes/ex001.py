from os import system
system("cls")
from rich import print

class Funcionario:
    def __init__(self, nome, cargo, setor):
        self.nome = nome
        self.cargo = cargo
        self.setor = setor

    def apresentacao(self):
        return f":trophy: Olá, sou [bold blue]{self.nome}[/] e sou {self.cargo} do setor  de {self.setor} da empresa Curso em Vídeo."
        

f1 = Funcionario("zacarias", "Programador", "TI")
print(f1.apresentacao())