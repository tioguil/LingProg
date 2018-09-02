# 14. Faça um programa que leia 5 números e informe o maior
# número.


list = []

for x in range(5):
    list.append(int(input("entre com um numero: ")))

print("Maior valor: ", max(list))