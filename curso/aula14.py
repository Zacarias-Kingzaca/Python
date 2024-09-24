from os import system
system("cls")

contador = 0 
while True:
    print("Contador:",contador)
    print("1 - Incrementar")
    print("2 - Encerrar")

    op=input("Escolhe uma op: ")
    
    if op == "1":
        contador += 1
    elif op == "2":
        break
    else:
        print("op inválida por favor escolhe a op 1 para incrementar e a 2 para encerrar")
        print("Programa encerrado, o contador final é:",contador)


