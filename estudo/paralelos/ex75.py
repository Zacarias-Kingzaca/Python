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

    def info_itens(self):
         return self._titulo, self._codigo

class Livro(ItemBiblioteca):
    def __init__(self, titulo, codigo):
        super().__init__(titulo, codigo)

    def emprestar(self):
            print(f"O livro {self._titulo} foi emprestado com sucesso!")
    def devolver(self):
            print(f"O livro{self._titulo} foi devolvido com sucesso!")
    def info_itens(self):
         print(f"Nome do Livro: {self._titulo}")
         print(f"Código do Livro: {self._codigo}")

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

lista = []
while True:
     system("cls")
     print("="*50)
     print(f"{"Biblioteca Zacarias":^50}")
     print("="*50)
     print("1 cadastar itens")
     print("2 emprestar ")
     print("3 devolver")
     print("4 ver itens")
     print("5 sair")
     try:
        op = input("Escolha: ")
     except:
        print("Valor inválido.")
        sleep("2")
        system("cls")

     if op == "1":
          while True:
            system("cls")
            print("="*50)
            print(f"{"Cadastrar Item":^50}")
            print("="*50)
            print("1 Livro")
            print("2 DVD")
            print("3 Revista")
            print("4 Voltar")
            try:
                op = input("Escolha: ")
            except:
                print("Valor inválido.")
                sleep("2")
                system("cls")

            if op == "1" or op == "2" or op == "3":
                    system("cls")
                    titulo = input("Titulo: ")
                    codigo = input("Código: ")
                    if op == "1":
                        item = Livro(titulo, codigo)
                    elif op == "2":
                        item = DVD(titulo, codigo)
                    elif op == "3":
                        item = Revista(titulo, codigo)
                    lista.append(item)
                    print("Item cadastrado com sucesso!")
                    sleep(2)
            elif op == "4":
                    break
            else:
                print("Opção inválida...")
                sleep(2)
                system("cls")
                
     elif op == "2":
          system("cls")
          print("="*50)
          print(f"{"Emprestar Item":^50}")
          print("="*50)
          for i in lista:
               if len(lista) > 0:
                    codigo = input("Código do item a ser emprestado: ")
                    for i in lista:
                          if codigo == i.codigo:
                                i.emprestar()
                          else:
                               print("Item não encontrado")
                               operacao()
          else:
                    print("Nenhum item cadastrado...")
                    operacao()