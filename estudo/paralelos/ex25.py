from os import system
system("cls")
print()

class Funcionário:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    
    def aumentar_salario(self,porcentagem):
        aumento = self.salario * porcentagem / 100
        self.salario += aumento 
        print(f"O {self.nome}  terá o salário de: {self.salario:.2f}")
    

qunat = int(input("Número de funcinário: "))
for i in range(qunat):
    nome = input("Nome: ")
    salario = float(input("Salário: "))
    p = float(input("Porcentagem de aumento: %"))
    f = Funcionário(nome, salario)
    f.aumentar_salario(p)
    print("=========================")
    

