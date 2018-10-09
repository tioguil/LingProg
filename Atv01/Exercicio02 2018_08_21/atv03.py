# 3 Faça um programa que receba duas listas e retorne True se têm
# os mesmos elementos ou False caso contrário
# Duas listas possuem os mesmos elementos quando são compostas
# pelos mesmos valores, mas não obrigatoriamente na mesma ordem.

total_lista = 3

list1 = []
list2 = []

print("Lista 1")

for i in range(total_lista):
    list1.append(int(input()))
print("Lista 2")
for i in range(total_lista):
    list2.append(int(input()))
list1.sort()
list2.sort()

iguais = (list1 == list2)

print(iguais)