class House:
    def __init__(self, name, number_of_fioors):
        self.name = name
        self.number_of_fioors = number_of_fioors
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_fioors:    #  или второй вариан в виде двойного неравества
            for i in range(1,new_floor + 1): # +1 для того чтобы захватить последнее значение
                print(i) # вывод этажей от 1 до new_floor
        else:
            print("Такого этажа не существует") # вывод если этаж указан больше чем  number_of_fioors
    def __len__(self):
        return self.number_of_fioors
    def __str__(self):
        return f'Название:  {self.name} , кол-во этажей: {self.number_of_fioors}'


    def __eq__(self, other):
        return self.number_of_fioors == other.number_of_fioors # сравнивание кол-ва этажей
    def __lt__(self, other):
        return self.number_of_fioors < other.number_of_fioors  # (<)
    def __le__(self, other):
        return self.number_of_fioors <= other.number_of_fioors # (<=)

    def __gt__(self, other):
        return self.number_of_fioors > other.number_of_fioors    # (>)

    def __ge__(self, other):
        return self.number_of_fioors >= other.number_of_fioors    # (>=)

    def __ne__(self, other):
        return self.number_of_fioors  != other.number_of_fioors    # (!=)

    def __add__(self, value):
        self.number_of_fioors  += value
        return self

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self + other


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
