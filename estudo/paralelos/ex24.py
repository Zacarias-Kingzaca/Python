from os import system
system("cls")
print()


class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
      return sum(self.notas) / len(self.notas)
    
class Turma:
    def __init__(self):
      self.alunos = []

    def adicionar_aluno(self,aluno):
       self.alunos.append(aluno)

    def melhor_aluno(self):
       return max(self.alunos, key=lambda a: a.media())
    
turma = Turma()


num = int(input("Quantos alunos desejas cadastrar: "))

for _ in range(num):
   nome = str(input("Nome do Aluno: "))

   notas = []
   for i in range(3):
      nota = float(input(f"Digita a {i+1}º nota do {nome}: "))
      notas.append(nota)
   aluno = Aluno(nome, notas)
   turma.adicionar_aluno(aluno)
   
melhor = turma.melhor_aluno()
print(f"O melhor aluno é o {melhor.nome} com a média {melhor.media():.2f}")



#a1 = Aluno("Ana", [10, 10, 8.6])
#a2 = Aluno("Zacarias", [9, 7.0, 10])
#a3 = Aluno("Pedro", [8.5, 6, 8])
#turma.adicionar_aluno(a1)
#turma.adicionar_aluno(a2)
#turma.adicionar_aluno(a3)
