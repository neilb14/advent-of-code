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

if __name__ == '__main__':
        input = []
        key = ''
        for x in range(256):
            input.append(x)
            key += chr(x)
        lengths = [46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204]
        checksum_result = checksum(input, lengths, 0, 0)
        print(checksum_result[0]*checksum_result[1], ' ', hash(input, '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'))