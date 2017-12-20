import unittest
from solution import run

class TestSolution(unittest.TestCase):

    def test_run(self):
        path =     ['     |          ',
                    '     |  +--+    ',
                    '     A  |  C    ',
                    ' F---|----E|--+ ',
                    '     |  |  |  D ',
                    '     +B-+  +--+ ']
        self.assertEqual(run(path), 'ABCDEF')

if __name__ == '__main__':
    unittest.main()