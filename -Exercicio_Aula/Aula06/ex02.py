# 2 Defna a função div que recebe como argumentos dois números naturais m
#  e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não
# pode recorrer às operações aritmétcas de multplicação, divisão e resto da divisão
# inteira.
# Ex: div(7,2) = 3


def div(n,m):
    return 0 if n < m else 1 + div(n-m, m)

print(div(99,100))