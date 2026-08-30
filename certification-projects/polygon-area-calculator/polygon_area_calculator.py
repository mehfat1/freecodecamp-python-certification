from math import sqrt

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        self.width = width
    
    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return sqrt(self.width**2 + self.height**2)

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        size = ''
        for i in range(self.height):
            for i in range(self.width):
                size += '*'
            size += '\n'
        return size

    def get_amount_inside(self, shape: str) -> int:
        horizontal = self.width // shape.width
        vertical = self.height // shape.height
        return horizontal * vertical

    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side: int) -> None:
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side: int) -> None:
        self.height = side
        self.width = side

    def __str__(self) -> str:
        return f'Square(side={self.width})'

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
