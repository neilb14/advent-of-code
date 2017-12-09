import sys

def increment(x):
    return x+1

def decrement(x):
    return x-1

def move_right(matrix, i, j):
    if(matrix[i+1][j-1] == 0):
        return i+1, j, move_up
    return i+1, j, move_right

def move_up(matrix, i, j):
    if(matrix[i-1][j-1] == 0):
        return i, j-1, move_left
    return i, j-1, move_up

def move_left(matrix, i, j):
    if(matrix[i-1][j+1] == 0):
        return i-1, j, move_down
    return i-1, j, move_left

def move_down(matrix, i, j):
    if(matrix[i+1][j+1] == 0):
        return i, j+1, move_right
    return i, j+1, move_down

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
    result = 1
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

def calculate_sum(matrix, x, y):
    result = 0
    for i in range(x-1,x+2):
        for j in range(y-1, y+2):
            if(i == x and j == y):
                continue
            result += matrix[i][j]
    return result

def move(matrix, i, j):
    if(matrix[i-1][j] == 0):
        return i-1, j
    if(matrix[i][j-1] == 0):
        return i-1, j
    

def stress_of_square(n):
    matrix = [[0 for x in range(1000)] for y in range(1000)]
    center = 500
    i,j = center, center
    matrix[i][j] = 1
    result = 1
    move = move_right
    while(result < n):
        i,j,move = move(matrix, i, j)
        result = calculate_sum(matrix, i, j)
        matrix[i][j] = result
    return result

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(distance(n), ' ', stress_of_square(n))