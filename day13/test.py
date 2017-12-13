import unittest
from solution import run, safe_run

class TestSolution(unittest.TestCase):

    def test_run(self):
        commands = [
            '0: 3',
            '1: 2',
            '4: 4',
            '6: 4'
        ]
        self.assertEqual(run(commands, 0), 24)

    def test_safe_run(self):
        commands = [
            '0: 3',
            '1: 2',
            '4: 4',
            '6: 4'
        ]
        self.assertEqual(safe_run(commands), 10)

if __name__ == '__main__':
    unittest.main()