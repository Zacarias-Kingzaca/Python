from os import system
from op import operacao
system("cls")
print()


class ContaBancaria:
    def __init__(self, nome, saldo):
         self.nome = nome
         self.__saldo = saldo

    
    def depositar(self, valor):
        if valor > 0:
             self.__saldo += valor
        else:
            print("Impossível realizar tarefa")


    def  sacar(self, valor):
        if valor > 0 <= self.__saldo:
              self.__saldo -= valor
        else:
            print("Impossível realizar tarefa")


    def consultar(self):
        if self.__saldo:
            print(f'Saldo: {self.__saldo:.2f}kzs')
        else:
            print("Impossível realizar tarefa")

nome = input("Nome: ").title()
saldo = float(input("Saldo: ").strip())
conta = ContaBancaria(nome, saldo) 

while True:
     system("cls")
     print("2 - Sacar dinheiro")
     print("3 - Ver saldo")
     print("4 - Sair")
     op = input("Opcão: ")

     if op == "2":
         system("cls")
         valor = float(input("Valor: ").strip())
         conta.sacar(valor)
         operacao()

     elif op == "3":
         system("cls")
         conta.consultar()
         operacao()

     elif op == "4":
         system("cls")
         break
    