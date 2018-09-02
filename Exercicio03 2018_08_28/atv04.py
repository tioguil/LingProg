# 4. Faça um Programa que leia três números e mostre-os em ordem
# decrescente.

list = []

list.append(int(input("entre com primeiro valor")))
list.append(int(input("entre com segundo valor")))
list.append(int(input("entre com terceiro valor")))

list.sort()
list = reversed(list)

for a in list:
    print(a)