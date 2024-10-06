import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False
    
    def test_walk(self):
        """A method in which an object of the Runner class with an arbitrary name is created.
        Next, call the walk method on this object 10 times.
        Then use the assert Equal method to compare the distance of this object with the value 50"""
        ctg = runner.Runner('wolf')
        for i in range(10):
            ctg.walk()
        self.assertEqual(ctg.distance, 50)

    def test_run(self):
        """ A method in which an object of the Runner class with an arbitrary name is created. Next,
        call the run method on this object 10 times. Then use the assert Equal method to compare
        the distance of this object with the value 100 """
        ctg1 = runner.Runner("Alice")
        for i in range(10):
            ctg1.run()
        self.assertEqual(ctg1.distance, 100)

    def test_challenge(self):
        """A method in which 2 objects of the Runner class with arbitrary names are created. Next, the run and
         walk methods are called 10 times for objects, respectively. Since the distances must be different,
          use the assertNotEqual method to make sure that the results are unequal."""
        ctg2 = runner.Runner("hare")
        ctg3 = runner.Runner("kolobok")
        for i in range(10):
            ctg2.walk()
            ctg3.run()
        self.assertNotEqual(ctg2.distance, ctg3.distance)


if __name__ == "__main__":
    unittest.main()
