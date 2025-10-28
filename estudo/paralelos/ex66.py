from os import system
system("cls")
print()

class Animal:
    def falar(self):
        return "Som generico"
    
class Vaca(Animal):
    def falar(self):
        return "Muuuu!"
    
class Ovelha(Animal):
    def falar(self):
        return "Bééééé!"
    
animas = [Vaca(), Ovelha()]
for i in animas:
    print(i.falar())