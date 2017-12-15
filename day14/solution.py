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

def run(input):
    key = []
    for x in range(256):
        key.append(x)
    grid = [[0 for i in range(128)] for j in range(128)]
    result = 0
    for i in range(128):
        for x in hash(key, f'{input}-{i}'):
            result += sum([int(c) for c in bin(int(x,16))[2:]])
        #result += sum([int(c) for c in [bin(int(x,16)) for x in hash(key, f'{input}-{i}')][2:]])
    return result

if __name__ == '__main__':
        print(run('hfdlxzhv'))