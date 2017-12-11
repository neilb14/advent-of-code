import unittest
from solution import walk

class TestWalk(unittest.TestCase):

    def test_walk(self):
        self.assertEqual(walk('ne,ne,ne'), 3)
        self.assertEqual(walk('ne,ne,sw,sw'), 0)
        self.assertEqual(walk('ne,ne,s,s'), 2)
        self.assertEqual(walk('se,sw,se,sw,sw'), 3)
    
if __name__ == '__main__':
    unittest.main()