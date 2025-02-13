from os import system
system ("cls")
print()


n1 = float(input("Digita a primeira nota do aluno:"))
n2 = float(input("Digita a segumda nota do aluno: "))

media = (n1 + n2)/2 
if media > 5:
    print("Tendo {:.1f} e {:.1f}, a média do aluno é {:.1f} ".format(n1, n2, media))
    print("O aluno está Apto!")
elif media == 5:
    print("Tendo  {:.1f} e {:.1f} a média do aluno é {:.1f}".format(n1, n2, media))
    print("O aluno está em recuperação")
else:
    print("Tendo {:.1f} e {:.1f} a média do aluno é {:.1f} ".format(n1, n2, media))
    print("O aluno reprovou.") 