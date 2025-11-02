from os import system
from abc import ABC, abstractmethod
system("cls")
print()

#class abistrata
class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    
    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def mostrar_dados(self):
        pass

#Subclasses
class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base + 3000
    
    def mostrar_dados(self):
        print(f"Gerente: {self.nome}")
        print(f"Salário: {self.calcular_salario()}")

class Analista(Funcionario):
    def calcular_salario(self):
        return self.salario_base + 1000

    def mostrar_dados(self):
        print(f"Analista: {self.nome}")
        print(f"Salário: {self.calcular_salario()}")

class Estagiario(Funcionario):
    def calcular_salario(self):
        return self.salario_base
    
    def mostrar_dados(self):
        print(f"Estagiário: {self.nome}")
        print(f"Salário: {self.calcular_salario()}")

#Programa principal
funcionarios = []
quantos = int(input("Quantos funcionários deseja cadastrar? "))
for i in range(quantos):
    print(f"Cadastro do funcionário: {i+1}")
    nome = input("Nome: ")
    cargo = input("Cargo (gerente / analista / estagiario): ").lower()
    salario_base = float(input("Salário base: "))

    if cargo == "gerente":
        f = Gerente(nome, salario_base)
    elif cargo == "analista":
        f = Analista(nome, salario_base)
    elif cargo == "estagiario":
        f = Estagiario(nome, salario_base)
    else:
        print("Cargo inválido! Pulando...")
        continue
    funcionarios.append(f)
print("\n===Dados dos Funcionários===")
for f in funcionarios:
    f.mostrar_dados()

