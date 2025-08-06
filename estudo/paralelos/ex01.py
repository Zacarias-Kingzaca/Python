from os import system
system("cls")
print()

quad = [x**2 for x in range(1, 11)]
print(quad)
print()

pares = [x for x in range(1, 21) if x % 2 == 0]
print(pares)
print()

num = [f"o {x} é par" if x % 2 == 0 else f"o {x} é ímpar"  for x  in range(0, 10)]
print(num)
print()

texto = "python"
maiscula = [letra.upper() for letra in texto]
print(maiscula)
print()

listas = [[1, 2], [3, 4], [5, 6]]
valores = [num for linha in listas for num in linha]
print(valores)
print()

v = [-3, 0, 2, -1, 4]
par = [x**2 for x in v if x > 0 ]
print(par)