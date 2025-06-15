from os import system
system("cls")
print()

exp = str(input("Digita a expressão: "))
pilha = []
for simb in exp:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
         pilha.pop()
        else:
           pilha.append(")")
           break
if len(pilha) == 0:
   print("Sua expressão está válida.")
else:
   print("Sua expressão está errada.")