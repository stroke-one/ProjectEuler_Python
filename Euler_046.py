import time

tm = time.time()

class PComp():
    def __init__(self, max_val):
        self.primes = [0]*max_val
        
    def gen_primes(self):
        max_val = len(self.primes)
        for n in range(2, max_val):
            if self.primes[n] == 0:
                self.primes[n] = 2
                for e in range(n*n,max_val, n):
                    self.primes[e] = 1
        print("Primes done")

    def test_comp(self, position):
        for c in range(2, position-1):
            if self.primes[c] == 2:
                for k in range(1, int(position ** .5)):
                    if (c+(2*(k**2))) == position:
                        return(True)
        return(False)

p = PComp(10000)  # switch to yield so no need to find upper bound
p.gen_primes()

for n in range(len(p.primes)):
    if p.primes[n] == 1 and n%2 == 1:
        if p.test_comp(n) == False:
            print(n)
            break

print(time.time() - tm)
