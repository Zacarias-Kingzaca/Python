from os import system
from matematica import dobro,metade,porcentagem
system("cls")
print("")

print("*"*30)
print(f"{"CALCULE AQUI":^30}")
print("*"*30)

n = float(input("Digite um valor: "))
print("==============================")
print(f"O dobro  de {n} é {dobro(n)}")
print(f"A metade de {n} é {metade(n)}")
print("===============================")
while True:
    per = input("Desejas calcular a porcentagem também? [(Sim (s) / Não (n)]: ").upper().strip()
    if per in ["SIM", "S"]:
      taxa = float(input("Qual é a taxa? -> "))
      print(f"A porcentam de {taxa}% de {n} é {porcentagem(n,taxa)}")
      break
    elif per in ["NÃO", "N"]:
        break
    print("\033[1;31mPor favor digite apenas[(Sim (s) / Não (n)]\033[m")