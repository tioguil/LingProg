# 9 Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings
# possuem o mesmo comprimento e são iguais ou diferentes no
# conteúdo.
# Exemplo:
# String 1: Brasil Hexa 2018
# String 2: Brasil! Hexa 2018!
# Tamanho de "Brasil Hexa 2018": 16 caracteres
# Tamanho de "Brasil! Hexa 2018!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

print("Informe a primeira frase")
frase_um = input()
print("Informa a segunda frase")
frase_dois = input()

if  len(frase_um) ==len(frase_dois) and frase_um == frase_dois:
    print("As frases são iguais e tem o mesmo tamanho")
elif len(frase_um)==len(frase_dois) and frase_um != frase_dois:
    print("As frases tem o mesmo tamanho porem são diferentes")
else:
    print("As frases são diferentes e tem tamanhos diferentes")

print('Frase 1 "%s" - Tamanho: %s' % (frase_um, len(frase_um)))
print('Frase 2 "%s" - Tamanho: %s' % (frase_dois, len(frase_dois)))