from os import system
system ("cls")
print()

lar = float(input("Largura da parade: "))
alt = float(input("Altura da parede: "))
area = lar * alt

print("Sua parede tem a dimensão de {}x{} e sua área é de {}mq".format(lar, alt, area))

tinta = area / 2
print("para pintar essa parede, você precisará de {}L de tinta. ".format(tinta))