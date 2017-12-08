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

def halfway_captcha(input):
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
import sys

def captcha(input):
    result = 0
    last = None
    length = len(input)
    for i in range(0, length+1):
        digit = input[i%length]
        if last is not None and digit == last:
            result += int(digit)
        last = digit
    return result

def halfway_captcha(input):
    result = 0
    length = len(input)
    for i in range(0, length):
        digit = input[i%length]
        compare_to = input[int(((length/2)+i)%length)]
        if digit == compare_to:
            result += int(digit)
    return result

if __name__ == '__main__':
    print(captcha(sys.argv[1]), ' ', halfway_captcha(sys.argv[1]))