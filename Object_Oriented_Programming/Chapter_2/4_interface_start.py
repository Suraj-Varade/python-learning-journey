from abc import ABC, abstractmethod ## abstract base class

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f"{{'circle': {str(self.calcArea())}}}"

c = Circle(10)
print(c.calcArea()) # 314.0
print(c.toJSON()) # {'circle': 314.0}