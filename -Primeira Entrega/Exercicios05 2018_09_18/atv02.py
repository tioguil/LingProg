# 2 Figuras: Crie a seguinte hierarquia de classes de figuras geométricas.
# a. A classe abstrata Figura deve ter o método abstrato area.
# b. A classe concreta Circulo é subclasse de Figura.
# c. A classe abstrata Poligono é subclasse de Figura e deve ter os
# atributos base e altura .
# d. As classes concretas Triangulo, Losango, Retangulo e Quadrado são
# subclasses de Poligono. Tente criar mais uma generalização aqui olhando as fórmulas
# da área.
# e. Os polígonos Retangulo e Quadrado devem implementar a interface
# Diagonal, que deve ter um método que calcula a diagonal.
# f. Crie uma classe Geometria com uma lista de Figuras com pelo menos
# uma figura de cada e imprima suas áreas, perímetros e diagonais.


from abc import ABC, abstractmethod
import math

class Figura(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def area(self):
        pass

class Circulo(Figura):

    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def area(self):
        return str(math.pi * (self.raio ** 2))

    def perimetro(self):
        return 2 * math.pi * self.raio

class Poligono(Figura, ABC):

    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        pass


class Diagonal(ABC):

    def __init__(self):
        super().__init__()

    def diagonal(self):
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

class Triangulo(Poligono):

    def __init__(self, base, altura):
        super().__init__(base, altura)

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        pass

class Losango(Poligono):

    def __init__(self, base, altura):
        super().__init__(base, altura)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base * 2 + self.altura * 2

class Retangulo(Poligono, Diagonal):

    def __init__(self, base, altura):
        Poligono.__init__(self, base, altura)
        Diagonal.__init__(self)

    def area(self):
        return self.base * self.altura

    def diagonal(self):
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

    def perimetro(self):
        return self.base * 2 + self.altura * 2

class Quadrado(Poligono, Diagonal):

    def __init__(self, base, altura):
        Poligono.__init__(self, base, altura)
        Diagonal.__init__(self)

    def diagonal(self):
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2


class Geometria:

    def __init__(self):
        self.figuras = [
            Circulo(25),
            Triangulo(10, 20),
            Losango(12, 24),
            Retangulo(16, 8),
            Quadrado(10, 10)
        ]


for figura in Geometria().figuras:
    print("Área: ", figura.area())
    print("Perímetro: ", str(figura.perimetro()) , "\n")