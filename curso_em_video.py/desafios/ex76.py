from os import system
system("cls")
print()

materias_escolares = ( "Lápis", 50,
                       "Borracha", 80,
                       "Caderno",  250,
                       "Estjo", 200,
                       "Transferidor", 100,
                       "Compasso", 300,
                       "Mochila", 2000,
                       "Caneta", 100,
                       "Livro", 1000,
                      )
print(50*"-")  
print(f"{"Lista de preços":^50}")
print(50*"-")
for pos in range(0, len(materias_escolares)):
    if pos % 2 == 0:
     print(f"{materias_escolares[pos]:.<30}", end="")
    else:
       print(f"kzs{materias_escolares[pos]:>10.2f}") 