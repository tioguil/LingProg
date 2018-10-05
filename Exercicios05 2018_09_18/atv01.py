# 1 Linha: Crie a classe Linha que tem dois atributos, coordenada1 e coordenada2.
# Cada coordenada é uma tupla que carrega duas coordenadas cartesianas (x,yg que
# denotam pontos do segmento de reta. Faça métodos que calculem o comprimento
# do segmento de reta e sua inclinação.

import math
class Linha:


    def __init__(self, cod1, cod2):
        self.cod1 = cod1
        self.cod2 = cod2

    def comprimento(self):
        return math.sqrt((self.cod2[0] - self.cod1[0])**2 + (self.cod2[1] - self.cod1[1])**2)

    def inclinacao(self):
        return (self.cod2[1] - self.cod1[1]) / (self.cod2[0] - self.cod1[0])

    def __str__(self):
        return "Comprimento: " + str(self.comprimento()) + "\nInclinação: " + str(self.inclinacao())

print(Linha((6, 7), (10, 11)))