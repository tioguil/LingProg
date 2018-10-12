# 2 Faça um programa que receba duas listas e retorne True se são
# iguais ou False caso contrario.
# Duas listas são iguais se possuem os mesmos valores e na mesma
# ordem.

total_lista = 3

list1 = []
list2 = []

print("Lista 1")

for i in range(total_lista):
    list1.append(int(input()))
print("Lista 2")
for i in range(total_lista):
    list2.append(int(input()))

iguais = (list1 == list2)

print(iguais)