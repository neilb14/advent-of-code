import sys,re

def initialize(input):
    result = []
    layers = {}
    champion_depth = 0
    for layer in input:
        m = re.search('^(\d+):\s(\d+)$', layer)
        depth = int(m.group(1))
        layers[depth] = {
            'depth': depth,
            'range': int(m.group(2))
        }
        if(depth > champion_depth):
            champion_depth = depth
    for i in range(champion_depth+1):
        if(i in layers):
            result.append(layers[i])
        else:
            result.append({
                'depth': i,
                'range': 0
            })
    return result


def run(input,delay):
    firewall = initialize(input)
    count,result,caught = delay,0,False
    for layer in firewall:
        #print(f'[{count}] | {layer["depth"]}: {layer["range"]}')
        if(layer['range'] > 0):
            scan = count % (layer['range'] + layer['range']-2)
            if(scan == 0):
                caught = True
                #print(f'caught! [{count}] | {layer["depth"]}: {layer["range"]}')
                result += layer['depth'] * layer['range']
        count += 1
    if(caught and result <= 0):
        return 1
    return result

def safe_run(input):
    delay = 0
    while(True):
        #print(f' --- {delay} --- ')
        if(run(input,delay)==0):
            return delay
        delay +=1

if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        data = input_file.readlines()
        print(run(data, 0))
        print(safe_run(data))
