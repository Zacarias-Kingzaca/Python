from os import system
from op import operacao
system("cls")
print()

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
       try:
         return sum(self.notas) / len(self.notas)
       except:
          return 0

class Turma:
    def __init__(self):
     self.alunos = []

    def Adicionar_aluno(self, aluno):
       self.alunos.append(aluno)

    def mostrar_alunos(self):
       for i in self.alunos:
          print(f"Aluno: {i.nome}\nNotas: {i.notas}")
          print("="*30)
       else:
          return None

    def melhor_aluno(self):
       if self.alunos:
         return max(self.alunos, key=lambda a: a.media())
       else:
          return None
       

turma = Turma()


while True:
   print("1- Adicionar Aluno")
   print("2- Listar alunos")
   print("3- Mostrar melhor aluno")
   print("4- Sair")
   op = input("Escolha: ")

   if op == "1":
      system("cls")
      nome = input("Nome: ").title()
      notas = list(map(float, input("Digita três notas separada por espaço: ").split()))
      aluno = Aluno(nome, notas)
      turma.Adicionar_aluno(aluno)
      operacao()

   elif op == "2":
      system("cls")
      turma.mostrar_alunos()
      operacao()

   elif op == "3":
      system("cls")
      resultado = turma.melhor_aluno()
      print(f"O melhor aluno é o {resultado.nome} com a média {resultado.media()}")
      print()

   elif op == "4":
      system("cls")
      break
   
   else:
      print("Opcão inválida:")
      print()
      
      

#l1 = Aluno("zacarias", [12, 11, 11])
#l2 = Aluno("zaca", [12, 12, 12])

#turma.Adicionar_aluno(l1)
#turma.Adicionar_aluno(l2)
#turma.mostrar_alunos()
#result = turma.melhor_aluno()
#print(result.media())
 
       
       
       
          

 