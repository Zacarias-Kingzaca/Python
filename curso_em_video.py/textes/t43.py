from os import system
system ("cls")
print("")

print(30*"\033[1;37m-=-\033[m")
print("{:^90}".format("VERIFICA O SEU CPF"))
print(30*"\033[1;39m-=-\033[m")

cpf =(input("\033[1;mCPF:\033[m")).strip()
verificador = len(cpf)
if verificador == 11:
    print("\033[1;32mCPF VALÍDO\033[m")
else:
    print("\033[1;31mCPF INVÁLIDO\033[m")