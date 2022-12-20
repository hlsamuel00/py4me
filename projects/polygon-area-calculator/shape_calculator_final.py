class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50: return 'Too big for picture.'

        picture = ''
        for i in range(self.height):
            picture += '*' * self.width
            picture += '\n'
        return picture

    def get_amount_inside(self, other_shape):
        return self.get_area() // other_shape.get_area()



class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_side_length):
        super().set_height(new_side_length)
        super().set_width(new_side_length)

    def set_height(self, new_height):
        super().set_height(new_height)
        super().set_width(new_height)

    def set_width(self, new_width):
        super().set_width(new_width)
        super().set_height(new_width)
