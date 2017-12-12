import sys

def start_state(c, score, n):
    if(c == '{'):
        return nested_group(1), score, n
    if(c == '<'):
        return garbage(start_state), score, n
    if(c == '!'):
        return ignore(start_state), score, n
    return start_state, score, n

def nested_group(level):
    def group_state(c, score, n):
        if(c == '}'):
            return start_state if level <= 1 else nested_group(level-1), score+level, n
        if(c == '{'):
            return nested_group(level+1), score, n
        if(c == '!'):
            return ignore(group_state), score, n
        if(c == '<'):
            return garbage(group_state), score, n
        return group_state, score, n

    return group_state

def ignore(previous_state):
    def ignore_state(c, score, n):
        return previous_state, score, n

    return ignore_state

def garbage(previous_state):
    def garbage_state(c, score, n):
        if(c == '>'):
            return previous_state, score, n
        elif(c == '!'):
            return ignore(garbage_state), score, n
        else:
            return garbage_state, score, n+1

    return garbage_state

def run(input):
    score,state,n = 0,start_state,0
    for c in input:
        state,score,n = state(c, score, n)
    return score, n

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        data = input_file.read()
        print(run(data))