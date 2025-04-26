from os import system
system("cls")
print()

print("="*30)
print("{:^30}".format("VOTE NO SUA PREFERÊNCIA"))
print("="*30)
voto1 =  voto2 = voto3 = 0 
print("""

    [1] VOTE ZACARIAS
    [2] VOTE EDUARDO
    [3] VOTE JOÃO
        
    """)

for i in range(1, 21):
    escolha = int(input("ESCOLHA: "))
    while not escolha in [1,2,3]:
             print("ATT OPÇÃO ERRADA:")
             escolha = int(input("ESCOLHA: "))
    if escolha == 1:
        voto1 += 1
    elif escolha == 2:
        voto2 += 1
    elif escolha == 3:
         voto3 += 1
cand1 = (20 / 100) * voto1
cand2 = (20 / 100) * voto2
cand3 = (20 / 100) * voto3  

print(f"O candidato Zacarias tem a percentagem de {cand1:.2f}%")
print(f"O candidato Eduardo tem a percentagem de {cand2:.2f}%")
print(f"O candidato João tem a percentagem de {cand3:.2f}%")