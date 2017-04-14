import time

t = time.time()


class Truncatable():
    def __init__(self):
        self.primes = []

    def gen_primes(self, max_val):
        prime_test = {}
        for n in range(2, max_val):
            if not n in prime_test:
                prime_test[n] = 2
                for e in range(n*n, max_val, n):
                    prime_test[e] = 1
        self.primes = [k for k in prime_test if prime_test[k] == 2]

    def is_trunc(self, trunc_candidate):
        if trunc_candidate < 8: return False
        
        trunc_candidate = str(trunc_candidate)
        for n in range(1, len(trunc_candidate)):
            if not int(trunc_candidate[n:]) in self.primes:
                return(False)
            if not int(trunc_candidate[:-n]) in self.primes:
                return(False)
        return(True)
        
    

trunc = Truncatable()
trunc.gen_primes(900000)

prime_sum = 0
prime_hit = 0
for p in trunc.primes:
    if trunc.is_trunc(p):
        print(p)
        prime_sum += p
        prime_hit += 1
        if prime_hit == 11:
            break

print(prime_sum)

print(time.time() - t)
