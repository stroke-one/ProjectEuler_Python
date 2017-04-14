import time

t = time.time()

class CirclePrime():
    def __init__(self, max_val):
        self.prime_test = [0]*max_val
        self.prime_circles = 0
        
    def _is_circle(self, circle_candidate):
        p = str(circle_candidate)
        for n in range(len(p)-1):
            p = p[1:]+p[0]
            if not self.prime_test[int(p)] == 2:
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

    def test_for_circles(self):
        for p in range(len(self.prime_test)):
            if self.prime_test[p] == 2:
                if self._is_circle(p):
                    self.prime_circles += 1
        return()
    



circles = CirclePrime(1000000)
circles.gen_primes()
circles.test_for_circles()

print("Count is ", circles.prime_circles)
print(time.time() - t)
