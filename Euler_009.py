import time
import operator
import functools

t = time.time()

for a in range(1, 999):
    for b in range(1, 999-a):
        c = 1000-b-a
        if((a**2) + (b**2)) == c**2:
            print(a*b*c)
    


print(time.time() - t)

#time 0.015000104904174805


