# 4. Faça um Programa que leia três números e mostre-os em ordem
# decrescente.

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

if numero_2 > numero_1 and numero_1 > numero_3:
    print("%s - %s - %s" %(numero_2, numero_1, numero_3))
elif numero_2 > numero_1 and numero_3 > numero_2:
    print("%s - %s - %s" %(numero_3, numero_2, numero_1))
elif numero_2 > numero_3 and numero_3 > numero_1:
    print("%s - %s - %s" %(numero_2, numero_3, numero_1))
elif numero_1 > numero_2 and numero_3 > numero_1:
    print("%s - %s - %s" %(numero_3, numero_1, numero_2))
elif numero_1 > numero_2 and numero_3 > numero_2:
    print("%s - %s - %s" %(numero_1, numero_3, numero_2))
else:
    print("%s - %s - %s" %(numero_1, numero_2, numero_3))