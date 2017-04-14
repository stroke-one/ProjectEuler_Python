import time

t = time.time()
total = 0
for n in range(1, 1001):
    total += n**n

print(str(total)[-10:])
print(time.time() - t)
