import time
import calendar

t = time.time()


class Primer():
    def __init__(self, max_val):
        self.primes = [0] * max_val
        self.primes_c = []

    def gen_primes(self):
        max_val = len(self.primes)
        for n in range(2, max_val):
            if self.primes[n] == 0:
                self.primes[n] = 2
                if len(str(n)) == 4:
                    self.primes_c.append(n)
                for e in range(n * n, max_val, n):
                    self.primes[e] = 1
        print("Primes done")

    def isprime(self, prime_test):
        if self.primes[prime_test] == 2:
            return(True)
        return(False)

    def test_ab(self, a, b):
        n = 0
        while self.isprime(n**2 + a*n + b):
            n += 1
        return(n)


p = Primer(900000)
p.gen_primes()

max_count = 0
max_a, max_b = 0, 0

for a in range(-1000, 1000):
    for b in range(-1000, 1001):
        max_test =  p.test_ab(a, b)
        if max_test > max_count:
            max_count = max_test
            max_a, max_b = a, b

print("Coefficient a * b:", max_a * max_b)

print(time.time() - t)



































