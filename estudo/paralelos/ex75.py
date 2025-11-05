from os import system
from abc import ABC, abstractmethod
from op import operacao
from time import sleep
system("cls")
print()

class ItemBiblioteca(ABC):
    def __init__(self, titulo, codigo):
        self._titulo = titulo
        self._codigo = codigo
        
    @abstractmethod
    def emprestar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass

  

class Livro(ItemBiblioteca):
    def __init__(self, titulo, codigo):
        super().__init__(titulo, codigo)

    def emprestar(self):
            print(f"O livro {self._titulo} foi emprestado com sucesso!")
    def devolver(self):
            print(f"O livro {self._titulo} foi devolvido com sucesso!")
    

class DVD(ItemBiblioteca):
    def __init__(self, titulo, codigo):
          super().__init__(titulo, codigo)

    def emprestar(self):
         print(f"O DVD {self._titulo} foi emprestado com sucesso!")
    def devolver(self):
         print(f"O DVD {self._titulo} foi devolvido com sucesso!")


class Revista(ItemBiblioteca):
    def __init__(self, titulo, codigo):
          super().__init__(titulo, codigo)

    def emprestar(self):
         print(f"A revista {self._titulo} foi emprestado com sucesso!")
    def devolver(self):
         print(f"A revista {self._titulo} foi devolvido com sucesso!")
   

l = Livro("Outliers", 1)
d = DVD("RONG", 2)
r = Revista("New", 3)
lista = []
lista.append(l)
lista.append(d)
lista.append(r)
r.emprestar()
print()
r.devolver()
print()
l.emprestar()
print()
l.devolver()
print()
d.emprestar()
print()
d.devolver()