import unittest
from solution import distance, calculate_square

class TestCaptcha(unittest.TestCase):

    def test_calculate_square(self):
        square = calculate_square(3)
        self.assertEqual(len(square), 8)
        self.assertEqual(square[0], 1)
        self.assertEqual(square[1], 2)
        self.assertEqual(square[2], 1)
        self.assertEqual(square[3], 2)
        self.assertEqual(square[4], 1)
        self.assertEqual(square[5], 2)
        self.assertEqual(square[6], 1)
        self.assertEqual(square[7], 2)
        
    
    def test_distances(self):
        self.assertEqual(distance(1), 0)
        self.assertEqual(distance(12), 3)
        self.assertEqual(distance(23), 2)
        self.assertEqual(distance(1024), 31)
    
if __name__ == '__main__':
    unittest.main()