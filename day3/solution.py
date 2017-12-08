import sys

def increment(x):
    return x+1

def decrement(x):
    return x-1

def calculate_square(size):
    results = []
    max_r = size - 1
    min_r = int(size/2)
    r = max_r - 1
    f = decrement
    for i in range(0, (size*2) + (size-2)*2):
        results.append(r)
        if r >= max_r:
            f = decrement
        elif r <= min_r:
            f = increment
        r = f(r)
    return results

def distance(input):
    size = 1
    square = [0]
    result = 0
    position = 0
    i=1
    while(i <= input): 
        i += 1
        result = square[position]
        position +=1
        if(position >= len(square)):
            size += 2
            square = calculate_square(size)
            position = 0
    return result

if __name__ == '__main__':
    print(distance(int(sys.argv[1])))