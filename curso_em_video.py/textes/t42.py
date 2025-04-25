from os import system
system("cls")
print()
print(30*"=")
print("{:^30}".format("BANCO ZACARIAS"))
print(30*"=")
valor = int(input("Digita o valor a ser retirado: "))
total = valor
cedula = 100  
totcedula =  0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
          print(f"Saque feito com {totcedula} cédulas de {cedula} ")
        if cedula == 100:
           cedula = 50
        elif cedula == 50:
           cedula = 10
        elif cedula == 10:
           cedula = 1
           totcedula = 0
        if total == 0:
          break
