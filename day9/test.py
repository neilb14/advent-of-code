import unittest
from solution import start_state, nested_group, garbage, ignore, run

def fake_state(c, score):
    return fake_state, score

class TestSolution(unittest.TestCase):
    def test_start_state(self):
        self.assertEqual(start_state('{',0, 0)[0].__name__, 'group_state')
        self.assertEqual(start_state('<',0, 0 )[0].__name__, 'garbage_state')
        self.assertEqual(start_state('!',0, 0)[0].__name__, 'ignore_state')

    def test_group_state(self):
        state = nested_group(1)
        self.assertEqual(state('}',0, 0)[0], start_state)
        self.assertEqual(state('}',0, 0)[1], 1)

    def test_group_state(self):
        state = nested_group(1)
        self.assertEqual(state('}',0, 0)[0], start_state)
        self.assertEqual(state('}',0, 0)[1], 1)

    def test_nested_group_state(self):
        state = nested_group(2)
        self.assertEqual(state('}',0, 0)[0].__name__, 'group_state')
        self.assertEqual(state('}',0, 0)[1], 2)
        self.assertEqual(state('{',0, 0)[0].__name__, 'group_state')

    def test_ignore_state(self):
        state = ignore(fake_state)
        self.assertEqual(state('!',0, 0)[0], fake_state)
        self.assertEqual(ignore(fake_state)('>',0, 0)[0], fake_state)

    def test_garbage_state(self):
        state = garbage(fake_state)
        self.assertEqual(state('>',0, 0)[0], fake_state)
        self.assertEqual(state('<',0, 0)[0].__name__, 'garbage_state')
        self.assertEqual(state('!',0, 0)[0].__name__, 'ignore_state')
        self.assertEqual(state('{',0, 0)[0].__name__, 'garbage_state')
        self.assertEqual(state('}',0, 0)[0].__name__, 'garbage_state')

    def test_garbage_count(self):
        state = garbage(fake_state)
        self.assertEqual(state('>',0, 0)[2], 0)
        self.assertEqual(state('<',0, 0)[2], 1)
        self.assertEqual(state('!',0, 0)[2], 0)
        self.assertEqual(state('{',0, 0)[2], 1)
        self.assertEqual(state('}',0, 0)[2], 1)
        self.assertEqual(state('a',0, 0)[2], 1)

    def test_run_group_state_score(self):
        self.assertEqual(run('{}')[0], 1)
        self.assertEqual(run('{{}}')[0], 3)
        self.assertEqual(run('{{{}}}')[0], 6)
        self.assertEqual(run('{{{},{},{{}}}}')[0], 16)
        self.assertEqual(run('{<a>,<a>,<a>,<a>}')[0], 1)
        self.assertEqual(run('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0], 9)
        self.assertEqual(run('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0], 9)
        self.assertEqual(run('{{<a!>},{<a!>},{<a!>},{<ab>}}')[0], 3)

def test_run_garbage_count(self):
        self.assertEqual(run('<>')[1], 0)
        self.assertEqual(run('<random characters>')[1], 17)
        self.assertEqual(run('<<<<>')[1], 3)
        self.assertEqual(run('<{!>}>')[1], 2)
        self.assertEqual(run('<!!>')[1], 2)
        self.assertEqual(run('<!!!>>')[1], 0)
        self.assertEqual(run('<{o"i!a,<{i<a>')[1], 10)

if __name__ == '__main__':
    unittest.main()