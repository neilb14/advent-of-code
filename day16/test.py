import unittest
from solution import dance

class TestSolution(unittest.TestCase):

    def test_dance(self):
        dancers = [chr(i) for i in range(97,97+5)]
        self.assertEqual(''.join(dance(dancers[:], ['s1'])), 'eabcd')
        self.assertEqual(''.join(dance(dancers[:], ['s1', 'x3/4'])), 'eabdc')
        self.assertEqual(''.join(dance(dancers[:], ['s1', 'x3/4', 'pe/b'])), 'baedc')

if __name__ == '__main__':
    unittest.main()