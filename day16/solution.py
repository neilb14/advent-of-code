import sys,re

spin = re.compile('s(\d+)')
exchange = re.compile('x(\d+)\/(\d+)')
pair = re.compile('p(\w)\/(\w)')

def do_spin(dancers, step):
    n = int(spin.search(step).group(1))
    return dancers[-n:] + dancers[:-n]

def do_exchange(dancers, step):
    m = exchange.search(step)
    x = int(m.group(1))
    y = int(m.group(2))
    swap = dancers[x]
    dancers[x] = dancers[y]
    dancers[y] = swap
    return dancers

def do_pair(dancers, step):
    m = pair.search(step)
    x = m.group(1)
    y = m.group(2)
    index_x = dancers.index(x)
    index_y = dancers.index(y)
    dancers[index_x] = y
    dancers[index_y] = x
    return dancers

def dance(dancers, steps):
    for step in steps:
        if(spin.match(step)):
            dancers = do_spin(dancers, step)
        elif(exchange.match(step)):
            dancers = do_exchange(dancers, step)
        elif(pair.match(step)):
            dancers = do_pair(dancers, step)
        else:
            raise Exception(f'Error: unknown step [{step}]')
    return ''.join(dancers)

if __name__ == '__main__':
    dancers = [chr(i) for i in range(97,97+16)]
    with open(sys.argv[1], 'r') as input_file:
        steps = input_file.read().split(',')
        print(dance(dancers, steps))