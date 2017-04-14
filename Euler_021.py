import time

t = time.time()

def facts(n):
    divisors = [1]
    for test_number in range(2, int(n**.5)):
        if n % test_number == 0:
            divisors.append(test_number)
            divisors.append(n//test_number)
    return(divisors)

amicable = []
for test_limit in range(1, 10001):
    if not test_limit in amicable:
        a = sum(facts(test_limit))
        b = sum(facts(a))
        if (b == test_limit) and (b != a):
            amicable += [a, b]

print(sum(set(amicable)))

print(time.time() - t)
