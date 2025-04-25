from os import system
system("cls")
print()
n1 = n2 = n3 = 0
print(""" VOTE NO SEU PREFERIDO
      
        [ 1 ] Zacarias
        [ 2 ] Eduardo
        [ 3 ] João      
      """)

for i in range(1, 11):
    voto = int(input("ESCOLAHA UM CANDIDATO Nª: "))
    if voto == 1:
        n1 += 1
    elif voto == 2:
        n2 += 1
    elif voto == 3:
        n3 += 1
if n1 > n2 and n2 > n3:
    print(f"O participante  Zacarias venceu com {n1} votos.")
elif n2 > n1 and n2 > n3:
    print(f"O participante  Eduardo venceu com {n2} votos.")
elif n3 > n1 and n3 > n2:
    print(f"O participante  João venceu com {n3} votos.")
else:
    if n1 == n2 and n2 != n3:
        print(f"OS participantes Zacarias e Eduardo empataram com {n1} a {n2} votos ")
    elif n2 == n3 and n2 != n1:
        print(f"Os participantes Eduardo e João empataram com {n2} a {n3} votos")
    elif n3 == n1 and n3 != n2:
        print(f"Os participantes João e o Zacarias empataram com {n3} a {n1} votos ")