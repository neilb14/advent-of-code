import unittest
from solution import captcha, halfway_captcha

class TestCaptcha(unittest.TestCase):

    def test_captcha(self):
        self.assertEqual(captcha('1122'), 3)
        self.assertEqual(captcha('1111'), 4)
        self.assertEqual(captcha('1234'), 0)
        self.assertEqual(captcha('91212129'), 9)

    def test_halfway_captcha(self):
        self.assertEqual(halfway_captcha('1212'), 6)
        self.assertEqual(halfway_captcha('1221'), 0)
        self.assertEqual(halfway_captcha('123425'), 4)
        self.assertEqual(halfway_captcha('123123'), 12)
        self.assertEqual(halfway_captcha('12131415'), 4)

if __name__ == '__main__':
    unittest.main()