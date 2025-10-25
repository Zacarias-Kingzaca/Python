from os import system
system("cls")
print()


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    
    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.salario:.2f} Kzs")
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    
    def exibir(self):
        super().exibir()
        print(f"Setor: {self.setor}")


    def aumento(self):
        if self.setor.lower() == "ti":
            self.salario = 100000
            print(f"O funcionário {self.nome} vai passar a ganhar {self.salario:.2f} kzs")
        else:
            print(f"Seja Bem-vindo {self.nome}")

g1 = Gerente("Zaca", 100000, "TI")
g1.exibir()
g1.aumento()