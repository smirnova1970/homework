
#  from termcolor import colored   у меня не работает, нашла в инете , печатает цветным

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'orange', 'silver', 'metallic']
    # Допустимые цвета для окрашивания

    def __init__(self, owner: str, __model: str, __color: str,  __engine_power: int):
        self.owner = owner        # владелец транспорта. (владелец может меняться)
        self.__model = __model      # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power      # мощность двигателя. (мы не можем менять самостоятельно)
        self.__color = __color                # название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color.upper()}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
