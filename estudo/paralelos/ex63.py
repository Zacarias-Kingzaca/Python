from os import system
system("cls")
print()

class Animal:
    def __init__(self,  nome,):
        self.nome = nome

    
    def falar(self):
        print("")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)  

    def falar(self):
        print(f"O {self.nome} faz: AU AU")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)  

    def falar(self):
        print(f"O {self.nome} faz: Miua Miua")


class Vaca(Animal):
    def __init__(self, nome):
        super().__init__(nome)  

    def falar(self):
        print(f"O {self.nome} faz: Muuu Muuu")
    
n1 = Cachorro("ze")
n1.falar()
n2 = Gato("bichano")
n2.falar()
n3 = Cachorro("oldo")
n3.falar()