import unittest
from solution import run, Generator

class TestSolution(unittest.TestCase):

    def test_generator(self):
        generator = Generator(16807, 65)
        self.assertEqual(generator.next(), 1092455)
        self.assertEqual(generator.next(), 1181022009)
        self.assertEqual(generator.next(), 245556042)
        self.assertEqual(generator.next(), 1744312007)
        self.assertEqual(generator.next(), 1352636452)

    def test_run(self):
        self.assertEqual(run(65, 8921, 5), 1)

if __name__ == '__main__':
    unittest.main()