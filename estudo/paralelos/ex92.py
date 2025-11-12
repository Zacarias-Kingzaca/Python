from os import system
system("cls")
print()

with open("dados.bin", "wb") as arquivo:
    nome = "ana"
    idade = 25
    arquivo.write(nome.encode("utf-8"))
    arquivo.write(idade.to_bytes(1, byteorder="big"))

with open("dados.bin", "rb") as arquivo:
    nome_bytes = arquivo.read(3)
    idade_byte = arquivo.read(1)
    nome = nome_bytes.decode("utf-8")
    idade = int.from_bytes(idade_byte, byteorder="big")

print(f"Nome: {nome}, idade: {idade}")

