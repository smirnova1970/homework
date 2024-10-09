"""ссылка на документацию   https://docs.python.org/3/howto/logging.html"""

import logging
import unittest
import runner


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s | %(name)s")


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# first = Runner('Вася', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)

# t = Tournament(101, first, second)
# print(t.start())


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            runner1 = Runner('Вася', -3)
            if runner1.speed > 0:
                logging.info('" test_walk" выполнен успешно ')
            for i in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)

        except ValueError:
            logging.warning(f"Неверная скорость для Runner")

    def test_run(self):
        try:
            runner2 = Runner(567, 3)
            if isinstance(runner2.name, str):
                logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner\n{e}")

    def test_challenge(self):
        ctg2 = runner.Runner("hare")
        ctg3 = runner.Runner("kolobok")
        for i in range(10):
            ctg2.walk()
            ctg3.run()
        self.assertNotEqual(ctg2.distance, ctg3.distance)
        logging.warning('" test_challenge" выполнен успешно')


if __name__ == "__main__":
    unittest.main()
