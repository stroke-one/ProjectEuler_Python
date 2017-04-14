import time

t = time.time()

class prime():
    def __init__(self):
        self.primes = [2]
        
    def test(self, number):
        for n in self.primes:
            if number % n == 0:
                return
        self.primes.append(number)

num = 2
p = prime()
while 1:
    num += 1
    p.test(num)
    if len(p.primes) == 10001:
        print(p.primes[-1])
        break
    
print(time.time() - t)

#time 8.036999940872192
