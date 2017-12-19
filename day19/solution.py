import sys,re

def done(path, y, x, breadcrumbs):
    print(''.join([c for c in breadcrumbs if re.match('\w', c)]))
    exit()

def down(path, y, x, breadcrumbs):
    if(path[y][x] == ' '):
        None,None,done
    if(path[y][x] == '+'):
        return find_next(path, y, x, down)    
    breadcrumbs.append(path[y][x])
    return y+1, x, down

def up(path, y, x, breadcrumbs):
    if(path[y][x] == ' '):
        None,None,done
    if(path[y][x] == '+'):
        return find_next(path, y, x, up)    
    breadcrumbs.append(path[y][x])
    return y-1, x, up

def left(path, y, x, breadcrumbs):
    if(path[y][x] == ' '):
        None,None,done
    if(path[y][x] == '+'):
        return find_next(path, y, x, left)    
    breadcrumbs.append(path[y][x])
    return y, x-1, left

def right(path, y, x, breadcrumbs):
    if(path[y][x] == ' '):
        None,None,done
    if(path[y][x] == '+'):
        return find_next(path, y, x, right)
    return y, x-1, right


def make_path(input):
    size_x, size_y = len(input[0]),len(input)
    result = [['' for x in range(size_x)] for y in range(size_y) ]
    for j in range(size_y):
        for i in range(size_x):
            result[j][i] = input[j][i]
    return result

def find_start(path):
    for x in range(len(path[0])):
        if path[0][x] == '|':
            return x
    raise Exception('Unable to find start')

def find_next(path, y, x, direction):
    if(direction == down or direction == up):
        if(path[y][x+1] != ' '):
            return y, x+1, right
        if(path[y][x-1] != ' '):
            return y, x-1, left
    if(direction == left or direction == right):
        if(y+1 < len(path) and path[y+1][x] != ' '):
            return y+1, x, down
        if(y-1 >= 0 and path[y-1][x] != ' '):
            return y-1, x, up

def run(input):
    path = make_path(input)
    breadcrumbs = []
    y, x, direction = 0,find_start(path), down
    while(True):
        print(f'{y}|{x} => {path[y][x]}')
        breadcrumbs.append(path[y][x])
        y, x, direction = direction(path, y, x, breadcrumbs)

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        input = input_file.readlines() 
        print(run(input))