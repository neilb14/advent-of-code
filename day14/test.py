import unittest
from solution import run, hexToBin

class TestCaptcha(unittest.TestCase):
    def test_hexToBin(self):
        self.assertEqual(hexToBin('03'), '0000')

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