import unittest
from solution import run

class TestSolution(unittest.TestCase):

    def test_run(self):
        commands = [
            '0 <-> 2',
            '1 <-> 1',
            '2 <-> 0, 3, 4',
            '3 <-> 2, 4',
            '4 <-> 2, 3, 6',
            '5 <-> 6',
            '6 <-> 4, 5'
        ]
        self.assertEqual(run(commands)[0], 6)
        self.assertEqual(run(commands)[1], 2)
        
if __name__ == '__main__':
    unittest.main()