import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    def setUpClass(cls):
        cls.all_results = {}
        return all_results
    def setUp(self):
        self.runer_1 = rt.Runner('Усэйн', 10)
        self.runer_2 = rt.Runner('Андрей', 9)
        self.runer_3 = rt.Runner('Ник', 3)


    def tearDownClass(self):
        for x, y in cls.all_results.items():
            print(f'Тест: {x}')
            for key, value in y.items():
                print(f'\t{key}: {value.name}')


    def



