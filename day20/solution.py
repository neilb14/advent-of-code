import sys,re

command = re.compile('^p=<(.+)>, v=<(.+)>, a=<(.+)>$')

def add(a, b):
    result = [0,0,0]
    for i in range(3):
        result[i] = a[i] + b[i]
    return result

def run(input):
    count = 0
    particles = []
    for i in input:
        m = command.search(i)
        p = [int(x) for x in m.group(1).split(',')]
        v = [int(x) for x in m.group(2).split(',')]
        a = [int(x) for x in m.group(3).split(',')]
        particles.append({
            'p':p,
            'v':v,
            'a':a
        })
    for i in range(1000):
        for particle in particles:
            particle['v'] = add(particle['v'], particle['a'])
            particle['p'] = add(particle['p'], particle['v'])
    champion = 999999999
    result = 0
    for i in range(len(particles)):
        distance = 0
        for j in range(3):
            distance += abs(particles[i]['p'][j])
        if(distance < champion):
            champion = distance
            result = i
    return result, champion
    
if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        input = input_file.readlines()
        print(run(input))