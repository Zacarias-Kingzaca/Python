from os import system
system("cls")
print()

n1 = float(input("sigita a sua primeira nota: "))
n2 = float(input("sigita a sua primeira nota: "))

m = (n1+n2)/2
print("sua media foi {:.1f} ".format(m))

if m >= 6.0:
    print("Sua médika foi boa, Parabéns")
else:
    print("Sua média foi pessima, Estude mais")