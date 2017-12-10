import unittest
from solution import reverse, checksum

class TestCaptcha(unittest.TestCase):

    def test_first_length(self):
        position = 0
        self.assertEqual(reverse([0,1,2,3,4], 3, position), [2,1,0,3,4])

    def test_second_length(self):
        position = 3
        self.assertEqual(reverse([2,1,0,3,4], 4, position), [4,3,0,1,2])

    def test_third_length(self):
        position = 3
        self.assertEqual(reverse([4,3,0,1,2], 1, position), [4,3,0,1,2])

    def test_fourth_length(self):
        position = 1
        self.assertEqual(reverse([4,3,0,1,2], 5, position), [3,4,2,1,0])

    def test_checksum(self):
        position = 0
        self.assertEqual(checksum([0,1,2,3,4], [3,4,1,5], 0, 0), 12)

if __name__ == '__main__':
    unittest.main()