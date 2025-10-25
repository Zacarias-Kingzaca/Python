from os import system
system("cls")
print()


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


    def exibir(self):
        print(f"Nome: {self.nome} recebe {self.salario:.2f}kzs por mês")


class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    
    def exibir(self):
        super().exibir()
        print(f"Setor: {self.setor}")


g1 = Gerente("Ana", 1000000, "TI")
g1.exibir()
