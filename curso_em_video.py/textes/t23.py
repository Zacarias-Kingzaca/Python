from os import system
system ("cls")
print()
op = 0
n1 = int(input("Digita o Primeiro valor: "))
n2 = int(input("Digita o segundo valor: "))

print(30*"=")
print("{:^30}".format("ESCOLHA UMA OPÇÃO"))
print(30*"=")

op = print("""
       [ 1 ] SOMA
       [ 2 ] DIVISÃO
       [ 3 ] MULTIPLICAÇÃO
       [ 4 ] SUBITRAÇÃO   """)
op = int(input("OPÇÃO:   "))
if op == 1:
    soma = n1 + n2
    print(f"{n1} + {n2} = {soma}")
elif op == 2: 
    div = n1 / n2
    print(f"{n1} / {n2} = {div}")
elif op == 3:
    mult = n1 * n2
    print(f"{n1} x {n2} = {mult}")
elif op == 4:
     sub = n1 - n2
     print(f"{n1} - {n2} = {sub}")
else:
   print("Opção errada tente novamente...")