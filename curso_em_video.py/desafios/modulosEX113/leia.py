def leiaint(msg):   
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("\033[0;31mPor favor digite um valor int válido.\033[m")
            continue
        except(KeyboardInterrupt):
           print("\033[0;31mEntrda de dados interrompida pelo usuário\033[m")
           return 0
        else:
         return n


def leiareal(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("\033[0;31mPor favor digite um valor int válido.\033[m")
            continue
        except(KeyboardInterrupt):
           print("\033[0;31mEntrda de dados interrompida pelo usuário\033[m")
           return 0
        else:
         return n

