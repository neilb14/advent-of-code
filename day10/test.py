import unittest
from solution import reverse, checksum, hash, make_dense_hash

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

    def test_make_dense_hash(self):
        self.assertEqual(make_dense_hash([65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]), '%02x' % 64)

    def test_checksum(self):
        position = 0
        result, position, size = checksum([0,1,2,3,4], [3,4,1,5], 0, 0)
        self.assertEqual(result[0]*result[1], 12)

    def test_hash(self):
        key = []
        for x in range(256):
            key.append(x)
        self.assertEqual(hash(key,''), 'a2582a3a0e66e6e86e3812dcb672a272')
        self.assertEqual(hash(key,'AoC 2017'), '33efeb34ea91902bb2f59c9920caa6cd')
        self.assertEqual(hash(key,'1,2,3'), '3efbe78a8d82f29979031a4aa0b16a9d')
        self.assertEqual(hash(key,'1,2,4'), '63960835bcdc130f0b66d7ff4f6a5a8e')

if __name__ == '__main__':
    unittest.main()