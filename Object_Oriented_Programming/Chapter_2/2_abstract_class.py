from abc import ABC, abstractmethod ## abstract base class

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# g = GraphicShape()
c = Circle(10)
print(c.calcArea())
s = Square(10)
print(s.calcArea())
'''
314.0
100
'''
