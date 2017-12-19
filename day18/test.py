import unittest
from solution import run, registers

class TestSolution(unittest.TestCase):

    def test_snd(self):
        commands = ['snd 1', 'snd 2', 'snd 3']
        self.assertEqual(run(commands), 3)
    
    def test_set(self):
        commands = ['set a 5', 'set b 7', 'set c a']
        run(commands)
        self.assertEqual(registers['a'], 5)
        self.assertEqual(registers['b'], 7)
        self.assertEqual(registers['c'], 5)

    def test_snd_from_register(self):
        commands = ['set a 9', 'snd a']
        self.assertEqual(run(commands), 9)

    def test_add(self):
        commands = ['set a 8', 'add a 1']
        run(commands)
        self.assertEqual(registers['a'], 9)
    
    def test_add_registers(self):
        commands = ['set a 4', 'set b 3', 'add a b']
        run(commands)
        self.assertEqual(registers['a'], 7)

    def test_mul(self):
        commands = ['set a 2', 'mul a 4']
        run(commands)
        self.assertEqual(registers['a'], 8)
    
    def test_mul_registers(self):
        commands = ['set a 4', 'set b 3', 'mul a b']
        run(commands)
        self.assertEqual(registers['a'], 12)

    def test_mod(self):
        commands = ['set a 7', 'mod a 2']
        run(commands)
        self.assertEqual(registers['a'], 1)
    
    def test_mul_registers(self):
        commands = ['set a 17', 'set b 3', 'mod a b']
        run(commands)
        self.assertEqual(registers['a'], 2)

    def test_run(self):
        commands = [
            'set a 1',
            'add a 2',
            'mul a a',
            'mod a 5',
            'snd a',
            'set a 0',
            'rcv a',
            'jgz a -1',
            'set a 1',
            'jgz a -2'
        ]
        self.assertEqual(run(commands), 4)

if __name__ == '__main__':
    unittest.main()