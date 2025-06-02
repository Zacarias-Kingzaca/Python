from os import system
system("cls")
print()
numeros = "Zero", "Um", "Dois", "Três","Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Terese", "Catorze", "Quinze", "Desasseis","Desacete", "Desoito"; "Desanove", "Vinte"

while True:
    while True:
        n = int(input("Digita um valor de 1 a 20: "))
        if 0 <= n <= 20:
            break 
   
    print(f"Você digitou o número {numeros[n]}") 
    print()