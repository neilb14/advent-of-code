import sys,re

last_frequency = None
recovered = []

def value(arg):
    if(re.match('-?\d', arg.strip())):
        return int(arg)
    ensure(arg)
    return registers[arg]

def ensure(arg):
    if(arg in registers):
        return
    registers[arg] = 0
    
def do_set(args):
    ensure(args[1])
    registers[args[1]] = value(args[2])
    return args[-1]+1

def do_snd(args):
    global last_frequency
    last_frequency = value(args[1])
    return args[-1]+1

def do_add(args):
    ensure(args[1])
    registers[args[1]] += value(args[2])
    return args[-1]+1

def do_mul(args):
    ensure(args[1])
    registers[args[1]] *= value(args[2])
    return args[-1]+1

def do_mod(args):
    ensure(args[1])
    registers[args[1]] = registers[args[1]] % value(args[2])
    return args[-1]+1

def do_rcv(args):
    result = value(args[1])
    if(result == 0):
        return args[-1]+1
    recovered.append(last_frequency)
    return 99999

def do_jgz(args):
    result = value(args[1])
    offset = value(args[2])
    if(offset > 1):
        offset -= 1
    if(result > 0):
        return args[-1]+offset
    return args[-1]+1

vtable = {
    'set':do_set,
    'snd':do_snd,
    'add':do_add,
    'mul':do_mul,
    'mod':do_mod,
    'rcv':do_rcv,
    'jgz':do_jgz
}

registers = {}

def run(commands):
    i = 0
    count = 0
    while(i < len(commands)):
        args = commands[i].split()
        args.append(i)
        i=vtable[args[0]](args)
        count+=1
        
    return last_frequency

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        commands = input_file.readlines()
        print(run(commands))