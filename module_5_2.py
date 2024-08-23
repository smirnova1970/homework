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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))