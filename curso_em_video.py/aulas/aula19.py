from os import system
system("cls")
print()
angola = list()
provincia = dict()
for c in range(0, 3):
    provincia["pv"] = input("Provincía: ")
    provincia["sigla"] = input("Sigla: ")
    angola.append(provincia.copy())
for i in angola:
    for p in i.values():
        print(p, end=" ")
        print()
