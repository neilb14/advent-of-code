import unittest
from solution import walk

class TestWalk(unittest.TestCase):

    def test_walk(self):
        self.assertEqual(walk('ne,ne,ne'), 3)
        self.assertEqual(walk('ne,ne,sw,sw'), 0)
        self.assertEqual(walk('se,se,nw,nw'), 0)
        self.assertEqual(walk('ne,ne,s,s'), 2)
        self.assertEqual(walk('se,sw,se,sw,sw'), 3)
        self.assertEqual(walk('ne,nw,ne,nw,nw'), 3)

    def test_input(self):
        self.assertEqual(walk('sw,s,se'), 2)
        self.assertEqual(walk('sw,s,se,se,se,se,se,nw'),5)
        #self.assertEqual(walk('sw,s,se,se,se,se,se,nw,ne,ne,ne,ne,ne,n,n,ne,n,n,n,n,n'), )
    
if __name__ == '__main__':
    unittest.main()