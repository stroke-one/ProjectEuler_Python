import time
t = time.time()

print(sum([int(digit) for digit in list(str(2**100))]))

print(time.time() - t)
