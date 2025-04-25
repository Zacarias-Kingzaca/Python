from os import system
system("cls")
print()


print("=========================")
print("{:^25}".format("FATORIAL"))
print("=========================")
resultado = 1
op = " "
n = int(input("Digita um número para ver o seu fatorial: "))
for i in range(n, 0, -1):
  resultado *= i
  op += str(i)
  if i > 1:
      op += " x "
  else:
    op += " = "
print(op,resultado)