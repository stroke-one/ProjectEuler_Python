import time

t = time.time()

sum_squares = sum([n**2 for n in range(1, 101)])
squares_sum = sum(range(1, 101))**2

print(squares_sum - sum_squares)


print(time.time() - t)

#time 0.008999824523925781
