class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def Volume(self):
        face_area = super().area()
        return face_area * self.length
    def __str__(self):
        return f'length is {self.length}'


cub = Cube(3)
cub_area = cub.surface_area()
cub_vol = cub.Volume()
print(f' cub(3)  area = {cub_area}, volume = {cub_vol}     ')
print(f' using cub __str__() the {cub}')