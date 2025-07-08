from os import system
system("cls")
print()

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    
    if idade < 16:
        return f"Com {idade} anos: Não pode votar."
    elif  16 <= idade <= 18 or idade >= 65:
        return f"Com {idade} anos: Voto opcional."
    elif idade >= 18 and idade < 59:
        return f"Com {idade} anos: Voto obrigatório."


ano = int(input("DIgite o ano em que nasceste: "))
print(voto(ano))