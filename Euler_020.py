import time

t = time.time()

def factorial(n):
    val = 1
    for i in range(1, n+1):
        val *= i
    return(val)

print(sum([int(digit) for digit in str(factorial(100))]))

print(time.time() - t)
