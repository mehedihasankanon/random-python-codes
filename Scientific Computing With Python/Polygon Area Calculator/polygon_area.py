from math import floor

class Rectangle:
    def __init__(self, width=5, height=10):
        self.width = width
        self.height = height

    def set_width(self, val):
        self.width = val

    def set_height(self, val):
        self.height = val

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        st = "*" * self.get_width()
        return (st + "\n") * self.get_height()

    def get_amount_inside(self, other):
        return floor(self.width / other.width) * floor(self.height / other.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def set_width(self, a):
        self.width = a
        self.height = a

    def set_height(self, a):
        self.width = a
        self.height = a

    def set_side(self, a):
        self.width = a
        self.height = a

    def __str__(self):
        return f"Square(side={self.width})"
