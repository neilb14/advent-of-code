import unittest
from solution import run

class TestSolution(unittest.TestCase):

    def test_run(self):
        self.assertEqual(run([0,3,0,1,-3]), 10)

if __name__ == '__main__':
    unittest.main()