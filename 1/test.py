import unittest
from solution import captcha

class TestCaptcha(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(captcha('1122'), 3)
        self.assertEqual(captcha('1111'), 4)
        self.assertEqual(captcha('1234'), 0)
        self.assertEqual(captcha('91212129'), 9)

if __name__ == '__main__':
    unittest.main()