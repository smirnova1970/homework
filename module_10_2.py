"""Задача "За честь и отвагу!":
Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
Атрибут name - имя рыцаря. (str)
Атрибут power - сила рыцаря. (int)
А также метод run, в котором рыцарь будет сражаться с врагами:
При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
В процессе сражения количество врагов уменьшается на power текущего рыцаря.
По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось
<кол-во воинов> воинов."
После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
Пункты задачи:
Создайте класс Knight с соответствующими описанию свойствами.
Создайте и запустите 2 потока на основе класса Knight.
Выведите на экран строку об окончании битв.
"""
from threading import Thread
from time import sleep


class Knight(Thread):
    class Knight(Thread):
        count_of_enemy = 100
        count_of_days = 0

        def __init__(self, name, power):
            super().__init__()
            self.name = name
            self.power = power

        def run(self):
            print(f'{self.name}, на нас напали!')
            while self.count_of_enemy > 0:
                self.count_of_enemy = self.count_of_enemy - self.power
                self.count_of_days += 1
                sleep(1)
                print(f'{self.name} сражается {self.count_of_days} дней, осталось {self.count_of_enemy} воинов.\n')
            print(f'{self.name} одержал победу спустя {self.count_of_days} дней!')

    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    # Запуск потоков и остановка текущего
    # Вывод строки об окончании сражения

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print('Все битвы закончились!')
