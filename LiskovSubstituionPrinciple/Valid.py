'''
    This is an example of a class that follows the Liskov Substitution Principle.
    The class Square is a subclass of the class Shape and it behaves like a shape.
    It follows the Liskov Substitution Principle.
'''
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height
    

class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)
    
    def setWidth(self, width):
        self.width = width
        self.height = width
    
    def setHeight(self, height):
        self.height = height
        self.width = height


def increaseWidthByOne(shape):
    shape.setWidth(shape.width + 1)

# Test code
rect = Rectangle(10, 20)
increaseWidthByOne(rect)
print(rect.area()) # 220

square = Square(10)
increaseWidthByOne(square)
print(square.area()) # 121


