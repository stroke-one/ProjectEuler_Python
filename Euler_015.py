import time
import operator
import functools

t = time.time()

r = 20
d = 20

n = functools.reduce(operator.mul, [v for v in range(r+d, 0, -1)][:d], 1)
k = functools.reduce(operator.mul, [v for v in range(1, d+1)], 1)

print(n/k)

print(time.time() - t)
