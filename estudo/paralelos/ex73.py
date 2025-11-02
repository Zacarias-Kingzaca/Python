from os import system
from abc import ABC, abstractmethod
from op import operacao
system("cls")
print()


class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def info_veiculo(self):
        pass

    def get_marca(self):
        return self.__marca
        
    def get_modelo(self):
        return self.__modelo
    
    def get_ano(self):
        return self.__ano

class Carro(Veiculo):
    def mover(self):
        print(f"O  carro {self.get_marca()} move-se com a capacidade de carrega mais de 5 pessoas.")

    def info_veiculo(self):
        print(f"Marca do carro: {self.get_marca()}")
        print(f"Modelo do carro: {self.get_modelo()}")
        print(f"Ano do carro: {self.get_ano()}")


class Camiao(Veiculo):
    def mover(self):
        print(f"O  camiao {self.get_marca()} move-se com a capacidade de carrega 20 mil litros de água.")

    def info_veiculo(self):
        print(f"Marca do camião: {self.get_marca()}")
        print(f"Modelo do camião: {self.get_modelo()}")
        print(f"Ano do camião: {self.get_ano()}")


class Moto(Veiculo):
    def mover(self):
        print(f"A moto {self.get_marca()} move-se com a capacidade de carrega mais de 1 pessoas.")

    def info_veiculo(self):
        print(f"Marca da moto: {self.get_marca()}")
        print(f"Modelo da moto: {self.get_modelo()}")
        print(f"Ano da moto: {self.get_ano()}")

veiculo = []
while True:
    print("1 Cadastrar carro")
    print("2 Cadastrar camião")
    print("3 Cadastrar moto")
    print("4 Sair")
    op = input("Opção: ")

    if op == "1" or op == "2" or op == "3":
        system("cls")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        if op == "1":
            c = Carro(marca, modelo, ano)
        elif op == "2":
            c = Camiao(marca, modelo, ano)
        elif op == "3":
            c = Camiao(marca, modelo, ano)
        veiculo.append(c)
        operacao()
    elif op == "4":
        system("cls")
        break
    else:
        system("cls")
        print("Opção inválida!")
        operacao()

for v in veiculo:
    v.info_veiculo()
    print("="*50)
    