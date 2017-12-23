import sys

def convert_input_string_to_list(input):
    for j in range(len(input)):
            input[j] = list(input[j].strip())
    return input

def up(x,y):
    return x,y-1

def down(x,y):
    return x,y+1

def left(x,y):
    return x-1,y

def right(x,y):
    return x+1,y

def resize(input):
    result = [['.' for x in range(len(input[0])+2)] for y in range(len(input)+2)]
    for i in range(len(input[0])):
        for j in range(len(input)):
            result[j+1][i+1] = input[j][i]
    return result

turn_right = {up:right, right:down, down:left, left:up}
turn_left = {up:left, left:down, down:right, right:up}
turn_back = {up:down, left:right, down:up, right:left}

def run(input, n):
    infected = 0
    x = int(len(input[0])/2)
    y = int(len(input)/2)
    direction = up
    for i in range(n):
        if(x < 0 or x >= len(input[0]) or y < 0 or y >= len(input)):
            input = resize(input)
            x +=1 
            y +=1
        node = input[y][x]
        if node == '.':
            input[y][x] = 'W'
            direction = turn_left[direction]
            x,y = direction(x,y)
        elif node == 'W':
            infected += 1
            input[y][x] = '#'
            x,y = direction(x,y)                        
        elif node == 'F':
            input[y][x] = '.'
            direction = turn_back[direction]
            x,y = direction(x,y)                                
        elif node == '#':
            input[y][x] = 'F'
            direction = turn_right[direction]
            x,y = direction(x,y)
        else:
            raise Exception('should not get here.')
    return infected

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        input = input_file.readlines() 
        print(run(convert_input_string_to_list(input), 10000000))