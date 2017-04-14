import time

t = time.time()

def get_prime(n):
    for x in range(2, n+1):
        if n % x == 0:
            return(x)
    return(n)

current = 600851475143
primes = []
while 1:
    test = get_prime(current)
    if test == current:
        print(current)
        break
    else:
        primes.append(test)
        current = int(current / test)
print(primes)

print(time.time() - t)

# finished in 0.014000177383422852
