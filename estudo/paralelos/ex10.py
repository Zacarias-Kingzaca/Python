from os import system
system("cls")
print()

def calculadora(n1, n2):
        print("      ESCOLHER OPERAÇÃO:")
        print("*"*30)
        print("""  
            [ 1 ] +
            [ 2 ] -
            [ 3 ] x
            [ 4 ] /
            """)
        print("*"*30)
        while True:
            op = (input("ESCOLHA -> "))
            if op not in ["1", "2", "3", "4"]:
                print("\033[1;31mOpção inválida escolhe novamente.\033[m")
            else:
                if op == "1":
                        resultado = n1 + n2
                        print(f"{n1} + {n2} = {resultado}")
                        break
                elif op == "2":
                        resultado = n1 - n2
                        print(f"{n1} - {n2} = {resultado}")
                        break
                elif op == "3":        
                        resultado = n1 * n2
                        print(f"{n1} x {n2} = {resultado}")
                        break
                elif op == "4":
                        resultado = n1 / n2
                        print(f"{n1} / {n2} = {resultado}")
                        break
            
                
print("-"*30)
print(f"{"CALCULADORA":^30}")
print("-"*30)
continuar = True
while True:            
    try:
        n1 = float(input("Valor de N1: "))
        n2 = float(input("Valor de N2: "))
        calculadora(n1, n2)
        perg =input("Quer continuar? [Sim (S) / Não (N)]: ").strip().upper()    
        while perg == "" or perg[0] not in "SN":
                    print("\033[1;31mPor favor digite apenas [Sim (S) / Não (N)]\033[m")
                    perg =input("Quer continuar? [Sim (S) / Não (N)]: ").strip().upper()
                    if perg[0] == "S":
                        break
                    if perg[0] == "N":
                        continuar = False
                        break  
                                   
    except ZeroDivisionError:
        print("\033[1;31mNão é possível dividir um número por 0 \033[m")
    except ValueError:
        print("\033[1;31mO valor que foi inserido é inválido \033[m")
    except IndexError:
        print("\033[1;31mO valor que foi inserido é inválido \033[m")
    finally:
        print("\033[1;32mSessão finalizada.\033[m")
        print()
    if continuar == False:
      break 
