import sys

def run(input):
    count = 0
    i = 0
    while(i >= 0 and i < len(input)):
        #print(f'{count}| {i} {input}')
        x = input[i]
        if(input[i] >= 3):
            input[i] -= 1
        else:
            input[i] += 1
        i = x + i
        count += 1
    return count

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        data = []
        for line in input_file.readlines():
            data.append(int(line))
        print(run(data))