import time

tm = time.time()

class Primer():
    def __init__(self, max_val):
        self.primes = [0]*max_val
        self.primes_c = []
        
    def gen_primes(self):
        max_val = len(self.primes)
        for n in range(2, max_val):
            if self.primes[n] == 0:
                self.primes[n] = 2
                if len(str(n)) == 4:
                    self.primes_c.append(n)
                for e in range(n*n,max_val, n):
                    self.primes[e] = 1
        print("Primes done")
        
        return()

p = Primer(9000)
p.gen_primes()

c = {}

while len(p.primes_c):
    x = p.primes_c.pop()
    for i in range(len(p.primes_c)):
        y = p.primes_c[i]
        if sorted(str(x)) == sorted(str(y)):
            dist = abs(x - y)
            srt  = sorted([x, y])
            if not dist in c:
                c[dist] = []
                c[dist].append(srt)
            elif not srt in c[dist]:
                c[dist].append(srt)
                

for k in c:
    while len(c[k]):
        i = c[k].pop()
        t = sorted(str(i[0]))
        for j in c[k]:
            if sorted(str(j[0])) == t:
                if i[0] < j[0]:
                    if i[1] == j[0]:
                        print(i, j)
                else:
                    if i[0] == j[1]:
                        print(i, j)
                    


print(time.time() - tm)
