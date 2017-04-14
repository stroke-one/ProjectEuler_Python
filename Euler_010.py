import time

t = time.time()

max_val = 2000001
p_test = {}

for n in range(2, max_val):
    if not n in p_test:
        p_test[n] = 2
        for e in range(n*n, max_val, n):
            p_test[e] = 1

print(sum([k for k in p_test if p_test[k] == 2]))

print(time.time() - t)

#time 2.0400002002716064
