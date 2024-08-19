class House:
    def __init__(self, name, number_of_fioors):
        self.name = name
        self.number_of_fioors = number_of_fioors
    def go_to(self, new_floor):
        if 0 < new_floor and new_floor <= self.number_of_fioors:
        # if 0 < new_floor <= self.number_of_fioors:    #  или второй вариан в виде двойного неравества
            for i in range(1,new_floor + 1): # +1 для того чтобы захватить последнее значение
                print(i) # вывод этажей от 1 до new_floor
        else:
            print("Такого этажа не существует") # вывод если этаж указан больше чем  number_of_fioors



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 10)
h1.go_to(22)
h2.go_to(5)