import sys

def reverse(input, length, position):
    first = []
    result = [None] * len(input)
    for x in range(length):
        first.append(input[(position+x)%len(input)])
    for x in range(len(input)):
        i = (position+x)%len(input)
        if(x < len(first)):
            result[i] = list(reversed(first))[x]
        else:
            result[i] = input[i]
    return result

def checksum(input, lengths, position, skip):
    if(len(lengths) <= 0):
        return input, position, skip
    return checksum(reverse(input, lengths[0], position), lengths[1:], (position + lengths[0] + skip)%len(input), skip+1)

def make_dense_hash(sparse_hash):
    result = 0
    for i in range(16):
        result = sparse_hash[i] ^ result
    return '%02x' % result

def hash(input, lengths):
    lengths_seq = [ord(c) for c in lengths] + [17,31,73,47,23]
    result = input
    position = 0
    skip = 0
    for i in range(64):
        result, position, skip = checksum(result, lengths_seq, position, skip)
    dense_hash = ''
    for x in range(16):
        start = x*16
        end = (x+1)*16
        dense_hash += make_dense_hash(result[start:end])
    return dense_hash

def print_grid(grid):
    for i in range(128):
        print(grid[i])

def mark(grid, i, j, count):
    if(i < 0 or j < 0 or i >= 128 or j >= 128 or grid[i][j] != 1):
        return
    grid[i][j] = count+100
    mark(grid, i-1, j, count)
    mark(grid, i+1, j, count)
    mark(grid, i, j-1, count)
    mark(grid, i, j+1, count)

def scan(grid):
    count = 0
    for i in range(128):
        for j in range(128):
            print(f'scan: [{i}][{j}]')
            if(grid[i][j] == 1):
                count += 1
                mark(grid, i, j, count)
    return count


def run(input):
    key = []
    for x in range(256):
        key.append(x)
    grid = [[0 for i in range(128)] for j in range(128)]
    result = 0
    for i in range(128):
        row = []
        for x in hash(key, f'{input}-{i}'):
            binary = [int(c) for c in bin(int(x,16))[2:]]
            row += [0 for y in range(4-len(binary))] + binary
        grid[i] = row
        result += sum(row)
    print_grid(grid)
    return result, scan(grid)

if __name__ == '__main__':
        print(run('hfdlxzhv'))