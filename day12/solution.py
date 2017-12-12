import sys, re

def count(groups, id, traversed):
    traversed[id] = True
    for x in groups[id]:
        if(x in traversed):
            continue
        count(groups, x, traversed)
    return len(traversed)

def walk(groups, id, walked):
    walked[id] = True
    for x in groups[id]:
        if(x in walked):
            continue
        walked = walk(groups, x, walked)
    return walked

def walk_all(groups):
    walked = {}
    count = 0
    for id in groups:
        if(id in walked):
            continue
        walked = walk(groups, id, walked)
        count+=1
    return count

def run(input):
    groups = {}
    for c in input:
        m = re.search('^(\d+)\s.{3}\s(.+)$', c)
        id = int(m.group(1))
        group = [int(x) for x in m.group(2).split(',')]
        if(not id in groups):
            groups[id] = []
        groups[id] += group
    return count(groups, 0, {}), walk_all(groups)

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        data = input_file.readlines()
        print(run(data))