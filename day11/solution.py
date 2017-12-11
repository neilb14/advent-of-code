import sys



def walk(input):
    path = {'n':0,'ne':0,'nw':0, 's':0, 'sw':0, 'se': 0}
    result = 0
    for step in input.split(','):        
        path[step] +=1
    for pair in [['ne','nw','n'],['se','sw','s']]:
        left, right = pair[0],pair[1]
        n = min(path[left],path[right])
        path[left] -=n
        path[right] -=n 
        path[pair[2]] += n
    for pair in [['ne','s','se'], ['nw','s','sw'], ['se','n','ne'], ['sw','n','nw']]:
        diagonal,vertical,to = pair[0],pair[1],pair[2]
        n = min(path[diagonal],path[vertical])
        path[diagonal] -=n
        path[vertical] -=n
        path[to] +=n    
    for pair in [['n','s'], ['ne','sw'], ['nw','ne']]:
        left, right = pair[0],pair[1]
        n = min(path[left],path[right])
        path[left] -=n
        path[right] -=n    
    for k in path:
        result += path[k]
    return result

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        data = input_file.read()
        print(walk(data))