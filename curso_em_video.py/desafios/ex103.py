from os import system
system("cls")
print()

def ficha(nome = '<Desconhecido>', gols = 0):
  print(f"O jogador {nome} fez {gols} gol(s) no campionato.")
       
print("========================")
nm = str(input('Nome do jogador: '))
g = str(input('Qauntos gols ele marcou: '))
if g.isnumeric():
  g = int(g)
else:
  g = 0
if nm.strip() == '':
    ficha(gols=g)
else:
    ficha(nm, g)