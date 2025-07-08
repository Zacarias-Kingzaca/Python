from os import system
system('cls')
print()

def fatorial(n, show=False):
    """
     -> Calcula o fatorial de um número.
    :parem n: O número a ser calculado.
    :parem show: (Opcional) mostrar ou não a conta.
    :return: Retorna o valor do fatorial de um número (n).
    """
    f = 1
    for c in range(n, 0, -1):
        if show :
            print(c, end=" ")
            if  c > 1:
             print(' x ', end=' ')
            else:
              print(' = ', end=' ')
        f *= c    
    return f


print(fatorial(5, True))
help(fatorial)
