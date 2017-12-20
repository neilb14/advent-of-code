import sys,re

command = re.compile('^p=<(.+)>, v=<(.+)>, a=<(.+)>$')

def add(a, b):
    result = [0,0,0]
    for i in range(3):
        result[i] = a[i] + b[i]
    return result

def check(c, p, i):
    x,y,z = p['p'][0],p['p'][1],p['p'][2]
    if x not in c:
        c[x] = {}
    if y not in c[x]:
        c[x][y] = {}
    if z not in c[x][y]:
        c[x][y][z] = []
    c[x][y][z].append(i)

def count_not_destroyed(particles):
    return len([x for x in particles if 'destroyed' not in x])

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
        collisions = {}
        for j in range(len(particles)):
            particle = particles[j]
            if 'destroyed' in particle:
                continue
            particle['v'] = add(particle['v'], particle['a'])
            particle['p'] = add(particle['p'], particle['v'])
            check(collisions, particle, j)
        for x in collisions:
            for y in collisions[x]:
                for z in collisions[x][y]:
                    if(len(collisions[x][y][z]) <= 1):
                        continue
                    for p in collisions[x][y][z]:
                        particles[p]['destroyed'] = True
    champion = 999999999
    result = 0
    for i in range(len(particles)):
        distance = 0
        for j in range(3):
            distance += abs(particles[i]['p'][j])
        if(distance < champion):
            champion = distance
            result = i
    return result, champion, count_not_destroyed(particles)
    
if __name__ == '__main__':
    with open(sys.argv[1], "r") as input_file:
        input = input_file.readlines()
        print(run(input))