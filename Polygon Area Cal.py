import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        total_space = self.width * self.height
        return total_space

    def get_perimeter(self):
        return (self.width + self.height)*2

    def get_diagonal(self):
        return math.hypot(self.width, self.height)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        final_pic = ""
        for r in range(self.height):
            for c in range(self.width):
                final_pic+="*"
            final_pic += "\n"
        return final_pic

    def get_amount_inside(self, shape):
        fits_in_width = 0
        current_w = self.width
        while current_w >= shape.width:
            fits_in_width += 1
            current_w -= shape.width
        fits_in_height = 0
        current_h = self.height
        while current_h >= shape.height:
            fits_in_height += 1
            current_h -= shape.height
        return fits_in_width * fits_in_height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)