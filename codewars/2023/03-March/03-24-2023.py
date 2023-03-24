# DESCRIPTION:
# Although shapes can be very different by nature, they can be sorted by the size of their area.

# Task:

# Create different shapes that can be part of a sortable list. The sort order is based on the size of their respective areas:
# The area of a Square is the square of its side
# The area of a Rectangle is width multiplied by height
# The area of a Triangle is base multiplied by height divided by 2
# The area of a Circle is the square of its radius multiplied by π
# The area of a CustomShape is given

# The default sort order of a list of shapes is ascending on area size:
# side = 1.1234
# radius = 1.1234
# base = 5
# height = 2

# # All classes must be subclasses of the Shape class

# shapes: List[Shape] = [Square(side), Circle(radius), Triangle(base, height)]
# shapes.sort()
# Use the correct π constant for your circle area calculations:
# math.pi

from math import pi

class Shape:
    def __init__(self, name: str = 'Shape') -> None:
        self.name = name
        self.area = int | float

    def __eq__(self, other: 'Shape') -> bool:
        return self.area == other.area
    
    def __lt__(self, other: 'Shape') -> bool:
        return self.area < other.area
    
    def __gt__(self, other: 'Shape') -> bool:
        return self.area > other.area
    
    def __le__(self, other: 'Shape') -> bool:
        return self.area <= other.area
    
    def __ge__(self, other: 'Shape') -> bool:
        return self.area >= other.area
    
    def __eq__(self, other: 'Shape') -> bool:
        return self.area == other.area
    
    def __ne__(self, other: 'Shape') -> bool:
        return self.area != other.area

class Rectangle(Shape):
    def __init__(self, width: float | int, height: float | int, name: str = 'Rectangle') -> None:
        super().__init__(name)
        self.width = width
        self.height = height
        self.area = width * height

class Square(Rectangle):
    def __init__(self, side: float | int) -> None:
        super().__init__(side, side, 'Square')

class Triangle(Shape):
    name = 'Triangle'
    def __init__(self, base: float | int, height: float | int) -> None:
        super().__init__('Triangle')
        self.base = base
        self.height = height
        self.area = (base * height) / 2

class Circle(Shape):
    def __init__(self, radius: float | int) -> None:
        super().__init__('Circle')
        self.radius = radius
        self.diameter = radius * 2
        self.area = (radius ** 2) * pi

class CustomShape(Shape):
    def __init__(self, area: float | int) -> None:
        super().__init__('CustomShape')
        self.area = area