from os import system
system("cls")
print()

dados = {}
Pessoas = []
stop = False
while True:
   if stop == True:
      break
   dados.clear()
   dados["nome"] = str(input("Nome: ").title())
   while True:
     dados["sexo"] = input("Sexo: [M/f] ").upper()[0]
     if dados["sexo"] in "MF":
        break
   dados["idade"] =  int(input("Idade: "))   
   Pessoas.append(dados.copy())
   per = input("Quer continuar [S/N]: ").upper()[0]
   if per in "Ss":
      pass
   elif per in "Nn":
      break
   else:
      while True:
         print("Digita apenas [S/N].")
         per = input("Quer continuar [S/N]: ")
         if per in "Ss":
            break
         elif per in "Nn":
            stop = True
            break
print("=-"*40)
soma = 0
for i in Pessoas: 
    soma += i["idade"]
media = soma / len(Pessoas)
print(f"A) Ao todo temos {len(Pessoas)} pessoas cadastradas.")
print(f"B) A média de idade é {media:.2f} anos")
print( "C) As mulheres cadastradas foram", end=" ")
for i in Pessoas: 
    if i["sexo"] in "Ff":
        print(f"{i["nome"]} ", end="")
print()
print( "D) As pessoas a sima de média são:")
for i in Pessoas:
   if i["idade"] >= media:
      print("        ", end="")
      for k, v in i.items():
         print(f"{k} = {v}; ", end="")
      print()
print("<<ENCERRADO>>")
      
