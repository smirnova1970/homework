class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        print(*cls.houses_history)
        return object.__new__(cls)
    def __init__(self, name, number_of_fioors):
        self.name = name
        self.number_of_fioors = number_of_fioors

    def __str__(self):
        return self.name
    def __del__(self):
        print({self.name} , 'снесён, но он останется в истории')






h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
