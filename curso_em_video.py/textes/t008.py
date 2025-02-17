from os import system
system ("cls")
print()


salario = float(input("Digita o seu salário: kzs"))

if salario < 2000:
    aumento = salario + (salario * 5 / 100) 
    
    print("Quem ganhava \033[1;31mkzs{:.2f}\033[m vai começar a ganhar \033[1;32mkzs{:.2f}\033[m".format(salario,aumento))
else:
    print("\033[1;31mSem aumento disponivel por agora\033[m")