from os import system
system("cls")
print()

palavras= ( "material",
       "programador",
       "estudar",
       "trabalhar",
       "gratis",
       "python",
       "curso")

for p in palavras:
    print(f"\n Na palavra {p.upper()} temos ", end=" " )
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")