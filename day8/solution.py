import sys,re

vtable = {
    '>' : lambda a,b: a > b,
    '>=' : lambda a,b: a >= b,
    '<' : lambda a,b: a < b,
    '<=' : lambda a,b: a <= b,
    '==' : lambda a,b: a == b,
    '!=' : lambda a,b: a != b
}

def initialize(registers, key):
    if(key in registers):
        return
    registers[key] = 0

def do_op(registers, key, op, value):
    if(op == 'inc'):
        registers[key] += value
    else:
        registers[key] -= value
    return registers[key]

def highest_value(registers):
    champion = 0
    for key in registers:
        challenger = registers[key]
        if(challenger > champion):
            champion = challenger
    return champion

def run(input):
    registers = {}
    champion = 0
    for command in input:
        register, op, value, junk, cond_register, cond_op, cond_value = command.split()
        initialize(registers, register)
        initialize(registers, cond_register)
        if(vtable[cond_op](registers[cond_register], int(cond_value))):
            challenger = do_op(registers, register, op, int(value))
            if(challenger > champion):
                champion = challenger
    
    return registers, highest_value(registers), champion

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        data = input_file.readlines()
        registers, highest, high_water_mark = run(data)
        print(f'{highest} {high_water_mark}')