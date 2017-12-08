import unittest
from solution import checksum_difference, checksum_divisible

class TestCaptcha(unittest.TestCase):

    def test_checksum_difference(self):
        self.assertEqual(checksum_difference('5 1 9 5\n7 5 3\n2 4 6 8'), 18)

    def test_checksum_divisible(self):
        self.assertEqual(checksum_divisible('5 9 2 8\n9 4 7 3\n3 8 6 5'), 9)

if __name__ == '__main__':
    unittest.main()