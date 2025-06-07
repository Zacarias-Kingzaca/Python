from os import system
system("cls")
print()

num = (int(input("digita um valor: ")), 
      int(input("digita um valor: ")),
      int(input("digita um valor: ")),
      int(input("digita um valor: ")),
      int(input("digita um valor: ")),
      int(input("digita um valor: ")))
print()
print(f"Maior valor digitado {max(num)}")
print(f"Menor valor digitado {min(num)}")