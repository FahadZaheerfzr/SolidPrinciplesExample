'''
    This is an example of a class that violates the Liskov Substitution Principle.
    The class Square is a subclass of the class Rectangle, but it does not behave
    like a rectangle. It violates the Liskov Substitution Principle.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square (Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
    

def increaseWidthByOne(rect):
    rect.set_width(rect.width + 1)


# Test code
rect = Rectangle(10, 20)
increaseWidthByOne(rect)
print(rect.get_area()) # 220

square = Square(10)
increaseWidthByOne(square)
print(square.get_area()) # 121

