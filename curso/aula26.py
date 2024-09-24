from os import system
system ("cls")
print("")
      
class Animal:
   def __init__(self, nome, especie):
      self.nome = nome
      self.especie = especie


   def fala(self):
       return f"{self.nome} é um(a) {self.especie}" 
   
class Cachoro(Animal):
   def __init__(self, nome, raca):
      super().__init__(nome, "Cachoro")
      self.raca = raca 
      
   def fala(self):
       return f"{super().fala()} e late" 


class Gato(Animal):
   def __init__(self, nome, cor):
      super().__init__(nome, "Gato")
      self.cor = cor 
      
   def fala(self):
       return f"{super().fala()} e mia" 
   

dog = Cachoro("Bilu","Caramelo")
cat = Gato("pipoca", "branco")

print("Atributo do Cachorro:")
print(f"Nome: {dog.nome}")
print(f"Raça: {dog.raca}")
print(f"Especie:{dog.especie}")
print()
print(dog.fala())

print()
print()

print("Atributo do Gato:")
print(f"Nome: {cat.nome}")
print(f"Raça: {cat.cor}")
print(f"Especie:{cat.especie}")
print()
print(cat.fala())


