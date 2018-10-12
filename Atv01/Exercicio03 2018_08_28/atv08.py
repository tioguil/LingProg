# 8. Faça um Programa que peça os 3 lados de um triângulo. O
# programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é:
# equilátero, isósceles ou escaleno.
# Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois
# lados for maior que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;

lado_a = float(input("Lado A"))
lado_b = float(input("Lado B"))
lado_c = float(input("Lado C"))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Os valores podem ser um triângulo.')
    if lado_a == lado_b == lado_c:
        print('Os valoresa formam um triângulo equilátero.')
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print('Os valores formam um triângulo isósceles.')
    else:
        print('Os valores formam um triângulo escaleno.')
else:
    print('Os valores não podem ser um triângulo.')