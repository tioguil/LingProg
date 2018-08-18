# Faça um Programa que peça 2 números inteiros e um número
# real. Calcule e mostre:
# - o produto do dobro do primeiro com metade do segundo .
# - a soma do triplo do primeiro com o terceiro.
# - o terceiro elevado ao cubo.


print("Informe primeiro numero inteiro")
numero1 = int(input())

print("Informe segundo numero inteiro")
numero2 = int(input())

print("Informe um numero Real")
numero3 = float(input())

res1 = (2*numero1)*(numero2/2)
res2 = (3*numero1)+numero3
res3 = (numero3**3)

print("o produto do dobro do primeiro com metade do segundo: ", res1)

print("a soma do triplo do primeiro com o terceiro: ", res2)

print("o terceiro elevado ao cubo: ", res3)