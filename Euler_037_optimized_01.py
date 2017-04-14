import time

t = time.time()

class Truncatable():
    def __init__(self, max_val):
        self.prime_test = [0]*max_val
        self.prime_sum = 0
        
    def _is_trunc(self, trunc_candidate):
        ## probably a better way to do this than strings
        trunc_candidate = str(trunc_candidate)
        for n in range(1, len(trunc_candidate)):
            if not self.prime_test[int(trunc_candidate[n:])] == 2:
                return(False)
            if not self.prime_test[int(trunc_candidate[:-n])] == 2:
                return(False)
        return(True)

    def gen_primes(self):
        max_val = len(self.prime_test)
        for n in range(2, max_val):
            if self.prime_test[n] == 0:
                self.prime_test[n] = 2
                for e in range(n*n,max_val, n):
                    self.prime_test[e] = 1
        return()

    def test_for_truncs(self):
        prime_hit = 0 # we know 11 total
        for p in range(8, len(self.prime_test)):
            if self.prime_test[p] == 2:
                if self._is_trunc(p):
                    self.prime_sum += p
                    prime_hit += 1
                    if prime_hit == 11:
                        break
        return()



trunc = Truncatable(1000000)
trunc.gen_primes()
trunc.test_for_truncs()
print("Sum is ", trunc.prime_sum)

print(time.time() - t)
