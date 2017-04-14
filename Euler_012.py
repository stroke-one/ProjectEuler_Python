import time

t = time.time()

def facts(triangle):
    factorials = []
    for n in range(1, int(triangle**.5)):
        if triangle % n == 0:
            factorials.append(n)
            factorials.append(triangle//n)
    return(len(factorials))


current_triangle = 1
current_step = 1
number_of_factorials = 0

while number_of_factorials < 500:
    current_step += 1
    current_triangle += current_step
    number_of_factorials = facts(current_triangle)

print(current_triangle)
print(number_of_factorials)
    

print(time.time() - t)
