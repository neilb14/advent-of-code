import unittest
from solution import dance

class TestSolution(unittest.TestCase):

    def test_dance(self):
        #steps = ['s1', 'x3/4', 'pe/b']
        self.assertEqual(dance([chr(i) for i in range(97,97+5)], ['s1']), 'eabcd')
        self.assertEqual(dance([chr(i) for i in range(97,97+5)], ['s1', 'x3/4']), 'eabdc')
        self.assertEqual(dance([chr(i) for i in range(97,97+5)], ['s1', 'x3/4', 'pe/b']), 'baedc')

if __name__ == '__main__':
    unittest.main()