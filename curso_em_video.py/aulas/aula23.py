from os import system
system("cls")
print()

try:
    a = int(input("Digita um número: "))
    b = int(input("Digita um número: "))
    r = a / b
except(ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possivel dividir um número por zero!")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados|!")
else:
    print(f"o resultado é {r:.2f}")
finally:
    print("Volte sempre! Muito obrigado.")
