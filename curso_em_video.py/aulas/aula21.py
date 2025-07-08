from os import system
system("cls")
print()

def par (num = 1):

   if n % 2 == 0:
      return True
   else:
      return False
n = int(input("Digita um número: "))
if par(n):
   print("É par")
else:
   print("Não é par")  
   