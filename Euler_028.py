import time

t = time.time()

total = 0
ticker = 0
n = 1
while n < 1001**2:
    countdown = 0
    ticker += 2
    while countdown < 4:
        total += n
        n += ticker
        countdown += 1
total += n

print(total)

print(time.time() - t)
