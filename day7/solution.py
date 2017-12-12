import sys,re

def run(input):
    parents = []
    children = []
    for yell in input:
        m = re.search('^(\w+)\s\((\d+)\)(.+)?$', yell)
        parents.append(m.group(1))
        weight = int(m.group(2))
        if(m.group(3)):
            children += [child.strip() for child in re.search('^\s.{2}\s(.+)', m.group(3)).group(1).split(',')]
    for child in children:
        if(child in parents):
            parents = [p for p in parents if p != child]
    print(len(parents))
    return parents[0]

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        data = input_file.readlines()
        print(run(data))