import unittest
from solution import start_state, nested_group, garbage, ignore, run

def fake_state(c, score):
    return fake_state, score

class TestSolution(unittest.TestCase):
    def test_start_state(self):
        self.assertEqual(start_state('{',0)[0].__name__, 'group_state')
        self.assertEqual(start_state('<',0)[0].__name__, 'garbage_state')
        self.assertEqual(start_state('!',0)[0].__name__, 'ignore_state')

    def test_group_state(self):
        state = nested_group(1)
        self.assertEqual(state('}',0)[0], start_state)
        self.assertEqual(state('}',0)[1], 1)

    def test_group_state(self):
        state = nested_group(1)
        self.assertEqual(state('}',0)[0], start_state)
        self.assertEqual(state('}',0)[1], 1)

    def test_nested_group_state(self):
        state = nested_group(2)
        self.assertEqual(state('}',0)[0].__name__, 'group_state')
        self.assertEqual(state('}',0)[1], 2)
        self.assertEqual(state('{',0)[0].__name__, 'group_state')

    def test_ignore_state(self):
        state = ignore(fake_state)
        self.assertEqual(state('!',0)[0], fake_state)
        self.assertEqual(ignore(fake_state)('>',0)[0], fake_state)

    def test_garbage_state(self):
        state = garbage(fake_state)
        self.assertEqual(state('>',0)[0], fake_state)
        self.assertEqual(state('<',0)[0].__name__, 'garbage_state')
        self.assertEqual(state('!',0)[0].__name__, 'ignore_state')
        self.assertEqual(state('{',0)[0].__name__, 'garbage_state')
        self.assertEqual(state('}',0)[0].__name__, 'garbage_state')

    def test_run_group_state_score(self):
        self.assertEqual(run('{}'), 1)
        self.assertEqual(run('{{}}'), 3)
        self.assertEqual(run('{{{}}}'), 6)
        self.assertEqual(run('{{{},{},{{}}}}'), 16)
        self.assertEqual(run('{<a>,<a>,<a>,<a>}'), 1)
        self.assertEqual(run('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
        self.assertEqual(run('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
        self.assertEqual(run('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)

if __name__ == '__main__':
    unittest.main()