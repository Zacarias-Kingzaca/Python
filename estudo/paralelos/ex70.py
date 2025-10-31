from os import system
from abc import ABC, abstractmethod
system("cls")
print()

class Funcionario(ABC):
    @abstractmethod
    def Calcular_Salario(self):
        pass

class Gerente(Funcionario):
    def Calcular_Salario(self, salario):
        self.salario = salario
        return f"Como o seu cargo é de Gerente o seu salário é {self.salario:.2f}kzs"
    
class Vendedor(Funcionario):
    def Calcular_Salario(self, slario):
        self.salario = slario
        com = self.salario * 20 / 100
        return f"Como o seu cargo é de Vendedor o seu salário é {self.salario + com:.2f}kzs"

f1 = Gerente()
print(f1.Calcular_Salario(1000))
f2 = Vendedor()
print(f2.Calcular_Salario(1000))
