import unittest
from solution import run, convert_input_string_to_list

class TestSolution(unittest.TestCase):

    def test_run_short(self):
        path =     ['..#',
                    '#..',
                    '...']
        self.assertEqual(run(convert_input_string_to_list(path), 7), 5)

    def test_run(self):
        path =     ['..#',
                    '#..',
                    '...']
        self.assertEqual(run(convert_input_string_to_list(path), 10000), 5587)

if __name__ == '__main__':
    unittest.main()