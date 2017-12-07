import sys

def captcha(input):
    result = 0
    first = input[0]
    last = None
    for digit in input:
        if last is not None and digit == last:
            result += int(digit)
        last = digit
    if first == last:
        result += int(last)
    return result

if __name__ == '__main__':
    print(captcha(sys.argv[1]))