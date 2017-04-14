import time
t = time.time()

def g(a, b):
    for nb in range(2, b+1):
        yield(a**nb)

a = 100
b = 100
c = []
for na in range(2, a+1):
    for term in g(na, b):
        if not term in c:
            c.append(term)

print(len(c))    

print(time.time() - t)
