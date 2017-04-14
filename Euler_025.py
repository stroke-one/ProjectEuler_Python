import time
t = time.time()
test = ""
a, b = 1, 1
index = 2

while len(test) < 1000:
    index += 1
    a, b = b, b + a
    test = str(b)
print(b, index)
print(time.time() - t)
    
    
