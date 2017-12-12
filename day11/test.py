import unittest
from solution import walk

class TestWalk(unittest.TestCase):

    def test_walk(self):
        self.assertEqual(walk('ne,ne,ne')[0], 3)
        self.assertEqual(walk('ne,ne,sw,sw')[0], 0)
        self.assertEqual(walk('se,se,nw,nw')[0], 0)
        self.assertEqual(walk('ne,ne,s,s')[0], 2)
        self.assertEqual(walk('se,sw,se,sw,sw')[0], 3)
        self.assertEqual(walk('ne,nw,ne,nw,nw')[0], 3)

    def test_furthest(self):
        self.assertEqual(walk('ne,ne,ne')[1], 3)
        self.assertEqual(walk('ne,ne,sw,sw')[1]], 2)
        self.assertEqual(walk('se,se,nw,nw')[1], 2)
        self.assertEqual(walk('ne,ne,s,s')[1], 2)
        self.assertEqual(walk('se,sw,se,sw,sw')[1], 3)
        self.assertEqual(walk('ne,nw,ne,nw,nw')[1], 3)

    def test_input(self):
        self.assertEqual(walk('sw,s,se')[0], 2)
        self.assertEqual(walk('sw,s,se,se,se,se,se,nw')[0],5)
    
if __name__ == '__main__':
    unittest.main()