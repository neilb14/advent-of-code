import sys

class Generator():
    def __init__(self, factor, start):
        self.factor = factor
        self.value = start

    def next(self):
        self.value = self.factor*self.value%2147483647
        return self.value

class SafeGenerator():
    def __init__(self, base, factor, start):
        self.base = base
        self.factor = factor
        self.value = start

    def next(self):
        self.value = self.factor*self.value%2147483647
        while(self.value % self.base != 0):
            self.value = self.factor*self.value%2147483647
        return self.value



def run(start_a, start_b, iters):
    count = 0
    gen_a = SafeGenerator(4,16807, start_a)
    gen_b = SafeGenerator(8,48271, start_b)
    for i in range(iters):
        a = gen_a.next()
        b = gen_b.next()
        if(((a ^ b) & 65535) == 0):
            count+=1
    return count

if __name__ == '__main__':
        print(run(512, 191, 5000000))