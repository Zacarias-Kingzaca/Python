from os import system
import re
system("cls")
print()

#EX1
res1 = re.findall(r"\b\w+(?=\spython)", "Curso de Java, curso de python, curso de JavaScript")
print(res1)
#EX2
res2 = re.findall(r"Curso de (?!python)\w+", "Curso de Java, curso de python, curso de JavaScript", re.I)
print(res2)
#EX3
res3 = re.findall(r"(?<=R)\d+", "R200, R400, R150")
print(res3)
#EX4
res4 = re.findall(r"(?<!@)\s\w+", "@Ana falou com pedro e o @joão ")
print(res4)
#EX5
res5 = re.findall(r"(?<=@)\w+(?=:)", "Mensagem de @Carlos: Olá! e @Maria: bom dia")
print(res5)
#EX6
res6 = re.findall(r"\d+(?=%)", "Desconto: 10%, 20%, 30, 40%")
print(res6)
#EX7
res7 = re.findall(r"(?<=,\s)\w+", "Ana, pedro, joão, carla")
print(res7)