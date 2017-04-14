import time
t = time.time()

def test(n):
    for x in range(1, 21):
        if not n % x == 0:
            return(False)
    return(True)

current = 0
while 1:
    current += 20
    if test(current):
        print(current)
        print("time", time.time() - t)
        break

# time 14.72000002861023
