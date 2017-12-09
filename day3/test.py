import unittest
from solution import distance, calculate_square, stress_of_square, calculate_sum

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

    def test_calculate_sum(self):
        square = [[1 for x in range(3)] for y in range(3)]
        self.assertEqual(calculate_sum(square, 1, 1), 8)

    def test_stress_of_square(self):
        self.assertEqual(stress_of_square(1), 1)
        self.assertEqual(stress_of_square(2), 2)
        self.assertEqual(stress_of_square(6), 10)
        self.assertEqual(stress_of_square(10), 10)
        self.assertEqual(stress_of_square(11), 11)
        self.assertEqual(stress_of_square(12), 23)
        self.assertEqual(stress_of_square(58), 59)
        self.assertEqual(stress_of_square(750), 806)
        
if __name__ == '__main__':
    unittest.main()