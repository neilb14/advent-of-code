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
        return input[0] * input[1]
    return checksum(reverse(input, lengths[0], position), lengths[1:], (position + lengths[0] + skip)%len(input), skip+1)

if __name__ == '__main__':
        input = []
        for x in range(256):
            input.append(x)
        lengths = [46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204]
        print(checksum(input, lengths, 0, 0))