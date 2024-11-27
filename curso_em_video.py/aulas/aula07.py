from os import system
system ("cls")
print()
 


n = s = 0

while True:
    n = int(input("Digita um valor: "))
    if n == 999:
        break
    s += n
print("A soma vale {}". format(s))