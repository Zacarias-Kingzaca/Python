from os import system
system("cls")

print("")

 
def soma(a,b):
 return a+b

def subtracao(a,b):
  return a-b

def multiplicacao(a,b):
 return a*b

def divisao(a,b):
 if a == 0:
  return "Erro: Divisão por zero!"
 return a/b

def menu():
   print(20*"=")
   print("Escolha OP:")
   print("1.Soma")
   print("2.Subtração")
   print("3.Multiplicação")
   print("4.Divisão")
   print("5.Sair")
   print(20*"=")


while True:
   menu()
   escolha=input("Digita sua op: ")
   if escolha == '5':
    print("calculadora fechada...")
    break
  

   n1 = float(input("Digita o primeiro número: "))
   n2 = float(input("Digita o segundo número: "))

   if escolha == '1':
    print(f" {n1:.0f}+{n2:.0f} = {soma(n1,n2)}")

   elif escolha == '2':
    print(f"{n1:.0f}-{n2:.0f} = {subtracao(n1,n2)}")
 
   elif escolha == '3':
    print(f"{n1:.0f}*{n2:.0f} = {multiplicacao(n1,n2)}")

   elif escolha == '2':
    print(f"{n1:.0f}/{n2:.0f} = {divisao(n1,n2)}")
     
   else:
    print("OP inválida...")

 