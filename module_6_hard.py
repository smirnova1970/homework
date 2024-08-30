import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: bool = True) -> None:
        if len(sides) != self.sides_count:
            self.__sides = [1*self.sides_count]
        else:
            self.__sides = [i for i in sides]
        self.__color = color
        self.filled = filled

    def get_color(self):
        return [i for i in self.__color]

    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        res = []
        for i in sides:
            if i > 0:
                res.append(i)
        if len(res) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):

    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        s = sum(self.get_sides()) / 2
        return math.sqrt(s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color,  *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count*[i for i in sides]
        else:
            self.__sides = [1*self.sides_count]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1]**3


circle1 = Circle((200, 200, 100), 10)   # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)    # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)   # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)   # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)    # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
