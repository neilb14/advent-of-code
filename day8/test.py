import unittest
from solution import run

class TestSolution(unittest.TestCase):

    def test_run(self):
        commands = [
            'b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10'
        ]
        result,champion = run(commands)
        self.assertEqual(result['b'], 0)
        self.assertEqual(result['a'], 1)
        self.assertEqual(result['c'], -10)
        self.assertEqual(champion, 1)

if __name__ == '__main__':
    unittest.main()