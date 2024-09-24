from os import system 
system("cls")
print("")

class Caneca:
    formato = "Cilindrico com alça lateral"
     
    def __init__(self,nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = "Cheia"
        self.preco = 1000
        self.__preco_fabrico = 500

    def beber(self):
        self.status = "Vazia"
        return f"É da {self.nome} que estou a beber "

    def encher(self):
        self.status = "Cheia"
        return f"É a {self.nome} que estou a enchedo"
    
