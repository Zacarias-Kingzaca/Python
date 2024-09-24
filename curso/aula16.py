from os import system
system("cls")
print("")

n = []


while True:

  numero = int(input("Digita um número inteiro: "))

  if numero == 0:
    break
  n.append(numero)

if n:
  
   print(f"A quantidade de elementos adicionados na lista é:{len(n)}")
   n_maior = [num for num in n if num != 0]
   print(f"O mair númerio digitado é: {max(n_maior)}")
   n_menor = [num for num in n if num != 0]
   print(f"O menor númerio digitado é: {min(n_menor)}")

else:
   print("Nenhum número foi adicionado na lista...")