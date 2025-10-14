from os import system
from op import operacao
system("cls")
print()

class Funcionario:
    def __init__(self, nome,cargo,salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario


class Empresa:
    def __init__(self):
        self.lista = []


    def adicionar_funcionario(self, funcionario):
        self.lista.append(funcionario)
        

    def listar_por_cargo(self, cargo):
        encontrou = False
        for c in self.lista:
            if c.cargo.lower() == cargo.lower():
                encontrou = True
                print(f"Nome do funcionário: {c.nome}")
                print(f"Cargo: {c.cargo}")
                print(f"Salário: {c.salario:.2f}kzs")
                print("=======================================")
        if not encontrou:
            print("Nenhum funcionário encontrado.")


    def salario_medio(self):
        if not self.lista:
            print("Nenhum funcionário encontrado.")
        total = sum(s.salario for s in self.lista)
        media = total / len(self.lista)
        print(f"A média de salário é de {media:.2f}Kzs")

empresa = Empresa()

while True:
    print("1 - Adicionar Funcionário")
    print("2 - Listar por cargo")
    print("3 - Salário médio")
    print("4 - Sair")
    op = input("Operação: ")

    if op == "1":
        system("cls")
        nome = input("Nome do funcionário: ").title()
        cargo = input("Cargo: ").capitalize()
        salario = float(input("Salário: ").strip())
        f = Funcionario(nome, cargo, salario)
        empresa.adicionar_funcionario(f)
        operacao()

    elif op == "2":
        system("cls")
        cargo = cargo = input("Cargo: ").capitalize()
        empresa.listar_por_cargo(cargo)
        operacao()

    elif op == "3":
        system("cls")
        empresa.salario_medio()
        operacao()

    elif op == "4":
        system("cls")
        break

    else:
        print("Opção inválida.")
        