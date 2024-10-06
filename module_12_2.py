import runner_and_tournament as rnt
import unittest

"""The Tournament class is a competition class where there is a distance to run and a list of participants. There 
is also the start method, which implements the logic of running along the proposed distance."""


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        """setUpClass is the method where the attribute of the all_results class is created. This is a dictionary in 
        which the results of all tests will be saved.
        setUp is a method where 3 objects are created:
        1.A runner named Hussein, with a speed of 10.
        2.A runner named Andrey, with a speed of 9.
        3.A runner named Nick, with a speed of 3."""
    def setUp(self):
        vs = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = {n: rnt.Runner(name=n, speed=v) for n, v in vs.items()}
    """tearDownClass is a method where all_results are output one by one in a column."""
    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{k}: {v}')
    """There are also methods for testing races in which a Tournament object is created for a distance of 90. The start 
    method is started for an object of the Tournament class, which returns the dictionary to the all_results variable. 
    At the end, the assertTrue method is called, which compares the last object from all_results (take by the largest 
    key) and the assumed name of the last runner.
    Write 3 such methods where they participate in the races (observe the order of transmission to the
    Tournament object):
    1. Usain and Nick
    2. Andrey and Nick
    3. Usain, Andrey and Nick."""
    def test_tournament_1(self):
        tour1 = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Ник'])
        result = tour1.start()
        # print(result)
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_tour1'] = result

    def test_tournament_2(self):
        tour2 = rnt.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
        result = tour2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_tour2'] = result

    def test_tournament_3(self):
        tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Андрей'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[list(all_results .keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = all_results


if __name__ == '__main__':
    unittest.main()
