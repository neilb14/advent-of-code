import sys

def start_state(c, score):
    if(c == '{'):
        return nested_group(1), score
    if(c == '<'):
        return garbage(start_state), score
    if(c == '!'):
        return ignore(start_state), score
    return start_state, score

def nested_group(level):
    def group_state(c, score):
        if(c == '}'):
            return start_state if level <= 1 else nested_group(level-1), score+level
        if(c == '{'):
            return nested_group(level+1), score
        if(c == '!'):
            return ignore(group_state), score
        if(c == '<'):
            return garbage(group_state), score
        return group_state, score

    return group_state

def ignore(previous_state):
    def ignore_state(c, score):
        return previous_state, score

    return ignore_state

def garbage(previous_state):
    def garbage_state(c, score):
        if(c == '>'):
            return previous_state, score
        if(c == '!'):
            return ignore(garbage_state), score
        return garbage_state, score

    return garbage_state

def run(input):
    score,state = 0,start_state
    for c in input:
        state,score = state(c, score)
    return score

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        data = input_file.read()
        print(run(data))