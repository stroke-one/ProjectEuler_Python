import time
t = time.time()

def collatz(n):
    if n == 1:
        return
    if n % 2 == 0:
        return(int(n/2))
    return((3*n)+1)

def run_collatz(current):
    terms = 0
    while current:
        current = collatz(current)
        terms += 1
    return(terms)
        
max_terms = 0
max_start = 0
for i in range(2, 1000000):
    test = run_collatz(i)
    if test > max_terms:
        max_terms = test
        max_start = i
print(max_start)

print(time.time() - t)    
