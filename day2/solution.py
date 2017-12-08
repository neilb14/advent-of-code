import sys

def checksum_difference(input):
    sum = 0
    for row in input.splitlines():
        big,small= 0, 999999
        for cell in row.split():
            if int(cell) > big:
                big = int(cell)
            if int(cell) < small:
                small = int(cell)
        sum += big-small
    return sum

def find_division(cells):
    values = []
    for cell in cells:
        value = int(cell)
        for check in values:
            pair = [check, value]
            if(max(pair)%min(pair) == 0):
                return int(max(pair)/min(pair))
        values.append(value)
    raise Exception("Oops!")


def checksum_divisible(input):
    sum = 0
    for row in input.splitlines():
        result = find_division(row.split())
        sum += result
    return sum

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        data = input_file.read()
        print(checksum_difference(data), ' ', checksum_divisible(data))